# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, division

class_names = [
    'back_ground', 'airplane', 'ship', 'storage tank', 'baseball diamond', 'tennis court',
 'basketball court', 'ground track field', 'harbor', 'bridge', 'vehicle']


classes_originID = {
    'airplane': 1, 'ship': 2, 'storage tank': 3, 'baseball diamond': 4,
    'tennis court': 5, 'basketball court': 6, 'ground track field': 7, 'harbor': 8, 'bridge': 9,
    'vehicle': 10}

originID_classes = {item: key for key, item in classes_originID.items()}
NAME_LABEL_MAP = dict(zip(class_names, range(len(class_names))))
LABEL_NAME_MAP = dict(zip(range(len(class_names)), class_names))

# print (originID_classes)



