import os
import sys
import importlib.util
import importlib

def load_numpy(version):
    if version == '1.26.4':
        numpy_path = os.path.abspath('numpy-1.26.4')
    elif version == '2.0.0':
        numpy_path = os.path.abspath('numpy-2.0.0')
    else:
        raise ValueError(f"Unsupported numpy version: {version}")

    # キャッシュをクリア
    if 'numpy' in sys.modules:
        del sys.modules['numpy']
    for mod_name in list(sys.modules):
        if mod_name.startswith('numpy'):
            del sys.modules[mod_name]

    # 環境変数を設定
    original_path = sys.path.copy()
    sys.path.insert(0, numpy_path)

    try:
        numpy_init_path = os.path.join(numpy_path, 'numpy', '__init__.py')
        spec = importlib.util.spec_from_file_location("numpy", numpy_init_path)
        if spec is None:
            raise ImportError(f"Cannot find numpy module in {numpy_path}")

        numpy = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(numpy)
    finally:
        # sys.pathを元に戻す
        sys.path = original_path

    return numpy
