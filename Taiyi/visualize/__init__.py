"""
结果可视化类，暂时通过第三方软件进行展示
"""
from collections import defaultdict
from .figure import Surface3d


class Visualization:
    def __init__(self, taiyi, visualize):
        self.taiyi = taiyi
        self.vis = visualize

    def show(self, epoch, ext=None):
        """
        1. 获取module_name
        2. 获取module_name 对应的 quantity
        2. 获取结果值 module:quantity:epoch
        :param ext:
        {
            'quantity':chart
            'ext_data':
            {
                'loss':
            }
        }
        :return:
        """
        logs = defaultdict(dict)
        module_names = self._get_module_name()
        for module_name in module_names:
            quantity_names = self._get_quantity_name(module_name)
            for quantity_name in quantity_names:
                key = module_name + '_' + quantity_name
                val = self._get_result(module_name, quantity_name, epoch)
                if val.size == 1:
                    val = val.item()
                else:
                    val = self._get_result(module_name, quantity_name)
                    val = Surface3d(val, key)
                logs[key] = val
        if ext is not None:
            logs.update(ext['ext_data'])
        self.vis.log(logs)

    def close(self):
        self.vis.finish()
        return

    def _get_module_name(self):
        module_names = self.taiyi.get_output().keys()
        return module_names

    def _get_quantity_name(self, module_name):
        quantity_name = self.taiyi.get_output()[module_name].keys()
        return quantity_name

    def _get_result(self, module_name, quantity_name, epoch=None):
        if epoch != None:
            value = self.taiyi.get_output()[module_name][quantity_name][epoch]
        else:
            value = self.taiyi.get_output()[module_name][quantity_name]
        return value
