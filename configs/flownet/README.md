# FlowNet

## Introduction

<!-- [ALGORITHM] -->

```bibtex
@inproceedings{dosovitskiy2015flownet,
  title={Flownet: Learning optical flow with convolutional networks},
  author={Dosovitskiy, Alexey and Fischer, Philipp and Ilg, Eddy and Hausser, Philip and Hazirbas, Caner and Golkov, Vladimir and Van Der Smagt, Patrick and Cremers, Daniel and Brox, Thomas},
  booktitle={Proceedings of the IEEE international conference on computer vision},
  pages={2758--2766},
  year={2015}
}
```

## Results and Models

<table>
    <thead>
        <tr>
            <td rowspan=2>Models</td>
            <td rowspan=2>Training datasets</td>
            <td rowspan=2>FlyingChairs</td>
            <td colspan=2>Sintel (training)</td>
            <td colspan=1>KITTI2012 (training)</td>
            <td rowspan=2>Log</td>
            <td rowspan=2>Config</td>
            <td rowspan=2>Download</td>
        </tr>
        <tr>
            <th>clean</th>
            <th>final</th>
            <th>EPE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>FlowNetC</th>
            <th>FlyingChairs</th>
            <th>1.78</th>
            <th>3.60</th>
            <th>4.93</th>
            <th>7.55</th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownetc_8x1_slong_flyingchairs_384x448.log.json'>log</a></th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownetc_8x1_slong_flyingchairs_384x448.py'>Config</a></th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownetc_8x1_slong_flyingchairs_384x448.pth'>Model</a></th>
        </tr>
        <tr>
            <th>FlowNetC</th>
            <th>Flying Chairs + FlyingThing3d subset</th>
            <th>2.57</th>
            <th>2.74</th>
            <th>4.52</th>
            <th>5.42</th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownetc_8x1_sfine_flyingthings3d_subset_384x768.log.json'>log</a></th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownetc_8x1_sfine_flyingthings3d_subset_384x768.py'>Config</a></th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownetc_8x1_sfine_flyingthings3d_subset_384x768.pth'>Model</a></th>
        </tr>
        <tr>
            <th>FlowNetC+ft</th>
            <th>Flying Chairs + Sintel</th>
            <th>2.80</th>
            <th>1.73</th>
            <th>2.09</th>
            <th>4.78</th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownetc_8x1_sfine_sintel_384x448.log.json'>log</a></th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownetc_8x1_sfine_sintel_384x448.py'>Config</a></th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownetc_8x1_sfine_sintel_384x448.pth'>Model</a></th>
        </tr>
        <tr>
            <th>FlowNetS</th>
            <th>FlyingChairs</th>
            <th>2.03</th>
            <th>4.25</th>
            <th>5.64</th>
            <th>8.81</th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownets_8x1_slong_flyingchairs_384x448.log.json'>log</a></th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownets_8x1_slong_flyingchairs_384x448.py'>Config</a></th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownets_8x1_slong_flyingchairs_384x448.pth'>Model</a></th>
        </tr>
        <tr>
            <th>FlowNetS+ft</th>
            <th>FlyingChairs + Sintel</th>
            <th>3.06</th>
            <th>1.93</th>
            <th>2.12</th>
            <th>6.83</th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownets_8x1_sfine_sintel_384x448.log.json'>log</a></th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownets_8x1_sfine_sintel_384x448.py'>Config</a></th>
            <th><a href='https://download.openmmlab.com/mmflow/flownet/flownets_8x1_sfine_sintel_384x448.pth'>Model</a></th>
        </tr>
    </tbody>
</table>
