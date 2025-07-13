# ⚖️ 用例对比

我们展示一些 MotrixSim 与 MuJoCo 之间仿真效果的对比，以让您直观的感受到 MotrixSim 的仿真优势

## 重力陀螺

重力陀螺的进动与章动仿真可以评估物理引擎对于接触点以及角动量仿真的准确性。

<div style="display: flex; gap: 20px; margin: 20px 0;">
  <div style="flex: 1;">
    <video controls loop autoplay style="width: 100%;">
      <source src="../../_static/videos/gyroscope_motrixsim.webm" type="video/webm">
    </video>
    <p style="text-align: center; font-weight: bold; margin-top: 10px;">MotrixSim</p>
  </div>
  <div style="flex: 1;">
    <video controls loop autoplay style="width: 100%;">
      <source src="../../_static/videos/gyroscope_mujoco.webm" type="video/webm">
    </video>
    <p style="text-align: center; font-weight: bold; margin-top: 10px;">MuJoCo</p>
  </div>
</div>

可以发现，MotrixSim 的物理效果更为真实，而 MuJoCo 仿真的陀螺在场景中出现不规则跑动。

MotrixSim 和 MuJoCo 使用同一份 mjcf 模型：[`gyroscope.xml`](../../../../examples/assets/gyroscope.xml).

您可以通过

::::{tab-set}
:sync-group: installation-mode

:::{tab-item} 使用 pip
:sync: pip

```bash
python examples/gyroscope.py
```

:::
:::{tab-item} 使用 uv
:sync: uv

```bash
uv run examples/gyroscope.py
```

:::
:::{tab-item} 使用 pdm
:sync: pdm

```bash
pdm run examples/gyroscope.py
```

:::

:::{tab-item} 使用 poetry
:sync: poetry

```bash
poetry run python examples/gyroscope.py
```

:::

::::

以及

::::{tab-set}
:sync-group: installation-mode

:::{tab-item} 使用 pip
:sync: pip

```bash
python examples/mujoco/gyroscope.py
```

:::
:::{tab-item} 使用 uv
:sync: uv

```bash
uv run examples/mujoco/gyroscope.py
```

:::
:::{tab-item} 使用 pdm
:sync: pdm

```bash
pdm run examples/mujoco/gyroscope.py
```

:::

:::{tab-item} 使用 poetry
:sync: poetry

```bash
poetry run python examples/mujoco/gyroscope.py
```

:::

::::

来运行这两个示例。

## 牛顿摆

牛顿摆是一个经典的物理演示，展示了刚体碰撞中的动量和能量守恒。

<div style="display: flex; gap: 20px; margin: 20px 0;">
  <div style="flex: 1;">
    <video controls loop autoplay style="width: 100%;">
      <source src="../../_static/videos/newton_cradle_motrixsim.webm" type="video/webm">
    </video>
    <p style="text-align: center; font-weight: bold; margin-top: 10px;">MotrixSim</p>
  </div>
  <div style="flex: 1;">
    <video controls loop autoplay style="width: 100%;">
      <source src="../../_static/videos/newton_cradle_mujoco.webm" type="video/webm">
    </video>
    <p style="text-align: center; font-weight: bold; margin-top: 10px;">MuJoCo</p>
  </div>
</div>

在这个例子中，MotrixSim 和 MuJoCo 使用了两份不同的 MJCF 文件：

-   MotrixSim: [`newton_cradle_mt.xml`](../../../../examples/assets/newton_cradle_mt.xml)
-   MuJoCo: [`newton_cradle_muj.xml`](../../../../examples/assets/newton_cradle_mj.xml)

因为 MuJoCo 只支持 Soft Contact， 而 MotrixSim 同时支持 Soft Contact 和 Hard Contact， 所以我们对 MJCF 作了一些扩展：

```xml
<geom solref="1 0" hard="true" />
```

这里的 `hard=true` 表示这是一个硬接触的几何体， 在此情况下， `solref=(bounciness, ERP)`表示弹性系数和 ERP（误差修正）的值。

您可以通过

::::{tab-set}
:sync-group: installation-mode

:::{tab-item} 使用 pip
:sync: pip

```bash
python examples/newton_cradle.py
```

:::
:::{tab-item} 使用 uv
:sync: uv

```bash
uv run examples/newton_cradle.py
```

:::
:::{tab-item} 使用 pdm
:sync: pdm

```bash
pdm run examples/newton_cradle.py
```

:::

:::{tab-item} 使用 poetry
:sync: poetry

```bash
poetry run python examples/newton_cradle.py
```

:::

::::

以及

::::{tab-set}
:sync-group: installation-mode

:::{tab-item} 使用 pip
:sync: pip

```bash
python examples/mujoco/newton_cradle.py
```

:::
:::{tab-item} 使用 uv
:sync: uv

```bash
uv run examples/mujoco/newton_cradle.py
```

:::
:::{tab-item} 使用 pdm
:sync: pdm

```bash
pdm run examples/mujoco/newton_cradle.py
```

:::

:::{tab-item} 使用 poetry
:sync: poetry

```bash
poetry run python examples/mujoco/newton_cradle.py
```

:::

::::

来运行这两个示例。

## Boston Dynamics Spot

该例子中，我们测试 MotrixSim 和 MuJoCo 在大时间步长下的稳定性。采用的模型为 Boston Dynamics Spot 机器人。

<div style="display: flex; gap: 20px; margin: 20px 0;">
  <div style="flex: 1;">
    <video controls loop autoplay style="width: 100%;">
      <source src="../../_static/videos/spot_motrixsim.webm" type="video/webm">
    </video>
    <p style="text-align: center; font-weight: bold; margin-top: 10px;">MotrixSim</p>
  </div>
  <div style="flex: 1;">
    <video controls loop autoplay style="width: 100%;">
      <source src="../../_static/videos/spot_mujoco.webm" type="video/webm">
    </video>
    <p style="text-align: center; font-weight: bold; margin-top: 10px;">MuJoCo</p>
  </div>
</div>

可以看到，MotrixSim 在大时间步长下仍然保持稳定，而 MuJoCo 则出现了明显的抖动和不稳定现象。

该模型取自 mujoco menagerie 仓库，然后我们将 timestep 修改为 0.01s，模型文件：[`spot.xml`](../../../../examples/assets/boston_dynamics_spot/spot.xml)。

您可以通过

::::{tab-set}
:sync-group: installation-mode

:::{tab-item} 使用 pip
:sync: pip

```bash
python examples/spot.py
```

:::
:::{tab-item} 使用 uv
:sync: uv

```bash
uv run examples/spot.py
```

:::
:::{tab-item} 使用 pdm
:sync: pdm

```bash
pdm run examples/spot.py
```

:::

:::{tab-item} 使用 poetry
:sync: poetry

```bash
poetry run python examples/spot.py
```

:::

::::

以及

::::{tab-set}
:sync-group: installation-mode

:::{tab-item} 使用 pip
:sync: pip

```bash
python -m mujoco.viewer --mjcf=examples/assets/boston_dynamics_spot/scene.xml
```

:::
:::{tab-item} 使用 uv
:sync: uv

```bash
uv run python -m mujoco.viewer --mjcf=examples/assets/boston_dynamics_spot/scene.xml
```

:::
:::{tab-item} 使用 pdm
:sync: pdm

```bash
pdm run python -m mujoco.viewer --mjcf=examples/assets/boston_dynamics_spot/scene.xml
```

:::
:::{tab-item} 使用 poetry
:sync: poetry

```bash
poetry run python -m mujoco.viewer --mjcf=examples/assets/boston_dynamics_spot/scene.xml
```

:::

::::

来运行这两个示例。

## 货架

该例子是我们内部在测试的一个场景，货架上摆放了大量的商品，可以评估物理引擎在处理复杂场景时的稳定性和准确性。

<div style="display: flex; gap: 20px; margin: 20px 0;">
  <div style="flex: 1;">
    <video controls loop autoplay style="width: 100%;">
      <source src="../../_static/videos/store_motrixsim.webm" type="video/webm">
    </video>
    <p style="text-align: center; font-weight: bold; margin-top: 10px;">MotrixSim</p>
  </div>
  <div style="flex: 1;">
    <video controls loop autoplay style="width: 100%;">
      <source src="../../_static/videos/store_mujoco.webm" type="video/webm">
    </video>
    <p style="text-align: center; font-weight: bold; margin-top: 10px;">MuJoCo</p>
  </div>
</div>

MotrixSim 在处理大量物体接触时表现稳定，而 MuJoCo 在这个场景中产生了物体抖动现象。

您可以通过

::::{tab-set}
:sync-group: installation-mode

:::{tab-item} 使用 pip
:sync: pip

```bash
python -m mujoco.viewer --file examples/assets/store/scene.xml
```

:::
:::{tab-item} 使用 uv
:sync: uv

```bash
uv run python -m mujoco.viewer --file examples/assets/store/scene.xml
```

:::
:::{tab-item} 使用 pdm
:sync: pdm

```bash
pdm run python -m mujoco.viewer --file examples/assets/store/scene.xml
```

:::
:::{tab-item} 使用 poetry
:sync: poetry

```bash
poetry run python -m mujoco.viewer --file examples/assets/store/scene.xml
```

:::

::::

以及

::::{tab-set}
:sync-group: installation-mode

:::{tab-item} 使用 pip
:sync: pip

```bash
python -m mujoco.viewer --mjcf=examples/assets/store/scene.xml
```

:::
:::{tab-item} 使用 uv
:sync: uv

```bash
uv run python -m mujoco.viewer --mjcf=examples/assets/store/scene.xml
```

:::
:::{tab-item} 使用 pdm
:sync: pdm

```bash
pdm run python -m mujoco.viewer --mjcf=examples/assets/store/scene.xml
```

:::
:::{tab-item} 使用 poetry
:sync: poetry

```bash
poetry run python -m mujoco.viewer --mjcf=examples/assets/store/scene.xml
```

:::

::::

来运行这两个示例。
