import scipy.io
import numpy as np
from pathlib import Path
from imagem_loader import ImageLoader
import cv2
import os

class LIVEDatabase:
    def __init__(self, database_path='data/databaserelease2'):
        self.database_path = Path(database_path)
        self.loader = ImageLoader()
        
        # Carregar metadados
        self.dmos = None
        self.ref_names = None
        self.load_metadata()
    
    def load_metadata(self):
        """Carrega os metadados da base LIVE"""
        try:
            # Carregar DMOS (Difference Mean Opinion Score)
            dmos_data = scipy.io.loadmat(self.database_path / 'dmos.mat')
            self.dmos = dmos_data['dmos'].flatten()
            
            # Carregar nomes das imagens de referência
            ref_names_data = scipy.io.loadmat(self.database_path / 'refnames_all.mat')
            self.ref_names = [name[0] for name in ref_names_data['refnames_all'].flatten()]
            
            print(f"✅ Base LIVE carregada: {len(self.ref_names)} imagens de referência")
            print(f"✅ DMOS disponíveis: {len(self.dmos)} scores")
            
        except Exception as e:
            print(f"⚠️  Erro ao carregar metadados LIVE: {e}")
            print("⚠️  Continuando sem DMOS...")
    
    def get_reference_images(self, limit=5):
        """Obtém imagens de referência da base"""
        ref_images = []
        ref_dir = self.database_path / 'refimgs'
        
        if not ref_dir.exists():
            print(f"❌ Diretório de referência não encontrado: {ref_dir}")
            return []
        
        # Procurar imagens
        image_files = list(ref_dir.glob('*.bmp'))  # LIVE usa .bmp
        
        if not image_files:
            # Tentar outros formatos
            for ext in ['*.jpg', '*.jpeg', '*.png', '*.tif']:
                image_files.extend(list(ref_dir.glob(ext)))
        
        # Selecionar imagens
        selected_images = []
        for i, img_path in enumerate(image_files[:limit]):
            # Copiar para data/reference para facilitar acesso
            dest_path = Path('data/reference') / f'ref_image_{i+1}.png'
            
            if not dest_path.exists():
                img = self.loader.load_image(str(img_path))
                cv2.imwrite(str(dest_path), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
            
            selected_images.append(str(dest_path))
            print(f"   ✅ {img_path.name} → {dest_path.name}")
        
        return selected_images
    
    def get_distorted_images(self, ref_name, distortion_type, level=None):
        """Obtém imagens distorcidas correspondentes a uma imagem de referência"""
        distortion_dirs = {
            'jpeg': 'jpeg',
            'jp2k': 'jp2k',
            'gblur': 'gblur',
            'wn': 'wn',
            'fastfading': 'fastfading'
        }
        
        if distortion_type not in distortion_dirs:
            print(f"❌ Tipo de distorção não suportado: {distortion_type}")
            return []
        
        dist_dir = self.database_path / distortion_dirs[distortion_type]
        
        if not dist_dir.exists():
            print(f"❌ Diretório de distorção não encontrado: {dist_dir}")
            return []
        
        # Encontrar imagens distorcidas para esta referência
        # No LIVE, os nomes são: refname_distortion.bmp
        base_name = Path(ref_name).stem
        pattern = f"{base_name}*.bmp"
        
        distorted_images = []
        for img_path in dist_dir.glob(pattern):
            distorted_images.append(str(img_path))
        
        # Se level for especificado, pegar uma específica
        if level is not None and distorted_images:
            level = min(level, len(distorted_images) - 1)
            return [distorted_images[level]]
        
        return distorted_images
    
    def get_distortion_levels(self, distortion_type):
        """Retorna os níveis de distorção disponíveis"""
        # Para LIVE, geralmente há 4-5 níveis por distorção
        levels_map = {
            'jpeg': [1, 2, 3, 4, 5],      # 5 níveis de compressão JPEG
            'jp2k': [1, 2, 3, 4, 5],      # 5 níveis de compressão JPEG2000
            'gblur': [1, 2, 3, 4, 5],     # 5 níveis de desfoque
            'wn': [1, 2, 3, 4, 5],        # 5 níveis de ruído branco
            'fastfading': [1, 2, 3, 4, 5] # 5 níveis de fading
        }
        
        return levels_map.get(distortion_type, [1, 2, 3, 4, 5])
    
    def get_dmos_for_image(self, ref_index, distortion_type, dist_index):
        """Obtém o DMOS para uma imagem distorcida específica"""
        if self.dmos is None:
            return None
        
        # No LIVE, as imagens estão organizadas em blocos
        # Cada bloco tem todas as distorções para uma imagem de referência
        distortion_order = ['jp2k', 'jpeg', 'wn', 'gblur', 'fastfading']
        
        if distortion_type not in distortion_order:
            return None
        
        # Calcular índice no array DMOS
        try:
            dist_pos = distortion_order.index(distortion_type)
            num_refs = len(self.ref_names)
            num_dist_per_ref = 5  # 5 distorções por imagem
            
            # Cada imagem tem 5 distorções × 5 níveis = 25 imagens distorcidas
            dmos_index = (ref_index * 25) + (dist_pos * 5) + dist_index
            return float(self.dmos[dmos_index])
        except:
            return None