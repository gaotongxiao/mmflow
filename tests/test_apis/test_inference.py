# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

import mmcv
import pytest
from mmcv.utils import Config

from mmflow.apis import inference_model, init_model
from mmflow.models import PWCNet


def test_init_model():
    cfg_file = '../../configs/_base_/models/pwcnet.py'
    cfg_file = osp.join(osp.dirname(__file__), cfg_file)
    cfg = Config.fromfile(cfg_file)

    model_from_cfg_file = init_model(config=cfg_file)
    model_from_cfg = init_model(config=cfg)

    assert isinstance(model_from_cfg_file, PWCNet)
    assert isinstance(model_from_cfg, PWCNet)


@pytest.mark.parametrize('cfg_file', [
    '../../configs/irr/irrpwc_8x1_sshort_flyingchairsocc_384x448.py',
    '../../configs/pwcnet/pwcnet_8x1_slong_flyingchairs_384x448.py'
])
def test_inference_model(cfg_file):
    cfg_file = osp.join(osp.dirname(__file__), cfg_file)
    model = init_model(config=cfg_file).cuda()

    img1_file = osp.join(osp.dirname(__file__), '../data/0000000-img_0.png')
    img2_file = osp.join(osp.dirname(__file__), '../data/0000000-img_1.png')

    flow_from_file = inference_model(model, img1s=img1_file, img2s=img2_file)

    img1 = mmcv.imread(img1_file)
    img2 = mmcv.imread(img2_file)

    flow_from_image = inference_model(model, img1s=img1, img2s=img2)

    H, W, _ = img1.shape

    assert flow_from_file.shape == (H, W, 2)
    assert flow_from_image.shape == (H, W, 2)
    assert flow_from_file.shape == (H, W, 2)
    assert flow_from_image.shape == (H, W, 2)
