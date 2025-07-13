# 📋 MJCF/URDF 文件

MJCF 与 URDF 是机器人仿真领域常用的两种模型格式。您可以通过以下两个链接了解更多 MJCF 与 URDF 的格式信息：

-   [MJCF 格式说明](https://mujoco.readthedocs.io/en/stable/XMLreference.html)
-   [URDF 格式说明](https://wiki.ros.org/urdf)

MotrixSim 在保持自己仿真能力特性的基础上，为 MJCF 与 URDF 提供了充分的兼容性支持。

您可以通过以下方式加载 MJCF 或 URDF 格式的机器人模型：

```py
import motrixsim
model = motrixsim.load_model("path/to/robot.xml")  # 加载 MJCF 格式的模型
```

or

```py
import motrixsim
model = motrixsim.load_model("path/to/robot.urdf") # 加载 URDF 格式的模型
```

我们推荐您尽量使用 MJCF 格式的模型文件，因为 MJCF 提供了更为强大的配置能力（包括丰富的组件、传感器、物理参数、渲染配置等等），而 URDF 则相对简单，仅支持基本的机器人模型描述。

尽管 MotrixSim 支持加载 URDF 格式，但为了构造更复杂场景，通常需要配合过程式构建 API，这部分能力 MotrixSim 尚未在 Python SDK 中暴露，但预计很快会提供。

## MJCF 支持情况

MJCF 包含了丰富的标签和属性，本章节会罗列 MotrixSim 当前版本对 MJCF 的支持情况。

### Global Configuration

```{list-table}
:header-rows: 1
:widths: 25 30 30 40
:class: longtable

* - **标签**
  - **已支持属性**
  - **计划支持属性**
  - **不支持属性**
* - option
  - timestep, gravity, iterations, tolerance
  - apirate, wind, magnetic, density, viscosity, o_margin, o_solref, o_solimp, o_friction, actuatorgroupdisable
  - impratio, integrator, cone, jacobian, solver, ls_iterations, ls_tolerance, noslip_iterations, noslip_tolerance, ccd_iterations, ccd_tolerance, sdf_iterations,  sdf_initpoints
* - compiler
  - autolimits, angle, eulerseq, meshdir, texturedir, assetdir
  - settotalmass, balanceinertia, strippath, discardvisual, usethread, inertiafromgeom, alignfree, inertiagrouprange, saveinertial, fitaabb
  - boundmass, boundinertia, coordinate, fusestatic
* - statistic
  - extent,center
  - meanmass, meaninertia, meansize
  - \\

```

不支持的标签：`size`

### Asset

已支持标签：

```{list-table}
:header-rows: 1
:widths: 25 50 40 20
:class: longtable
* - **标签**
  - **已支持属性**
  - **计划支持属性**
  - **不支持属性**
* - mesh
  - file, vertex, normal, texcoord, face, scale
  - content_type,  refpos, refquat, smoothnormal, maxhullvert, inertia
  - \\
* - hfield
  - file, nrow, ncol, elevation, size
  - content_type
  - \\
* - texture
  - type, file, builtin, rgb1, rgb2, width, height, colorspace
  - content_type, gridsize, gridlayout, fileright, fileleft, fileup, filedown, filefront, fileback, mark, markrgb, random, hflip, vflip, nchannel
  - \\
* - material
  - texture, rgba, texrepeat, texuniform, reflectance, metallic, roughness
  - emission, specular, shininess
  - \\
* - material/layer
  - texture, role
  - \\
  - \\
```

计划支持标签：

`skin`, `model`，`mesh/plugin`

```{note}
mesh 文件目前支持 stl、obj、dae 格式。

对于 texture 中的 type 属性，目前支持 2d, skybox, 不支持 cube。
```

### Scene

已支持标签：

```{list-table}
:header-rows: 1
:widths: 25 50 40 20
:class: longtable

* - **标签**
  - **已支持属性**
  - **计划支持属性**
  - **不支持属性**
* - body
  - mocap, pos, orientation, gravcomp
  - \\
  - \\
* - inertial
  - pos, orientation, mass, diaginertia, fullinertia
  - \\
  - \\
* - joint
  - pos, axis, springdamper, solreflimit, solimplimit, solreffriction, solimpfriction, stiffness, range, limited, actuatorfrcrange, actuatorfrclimited, margin, ref, springref, armature, damping, frictionloss
  - actuatorgravcomp
  - \\
* - geom
  - type, group, condim, contype, conaffinity, priority, size, mass, density, solmix, solref, solimp, margin, gap, fromto, pos, orientation, hfield, mesh
  - fitscale, fluidshape, fluidcoef, shellinertia
  - \\
* - geom.type
  - plane, hfield, sphere, capsule, cylinder, box, mesh
  - ellipsoid, sdf
  - \\
* - site
  - size, pos, orientation
  - type, group, material, rgb, fromto
  - \\
* - contact/exclude
  - body1, body2
  - \\
  - \\
* - camera
  - pos, orientation, orthographic, fovy, target
  - ipd, resolution, focal, focalpixel, principal, principalpixel, sensorsize
  - \\
* - camera.mode
  - fixed, track, targetbody
  - trackcom, targetbodycom
  - \\
* - light
  - pos, dir, target, type, directional, castshadow, diffuse, cutoff
  - active, bulbradius, intensity, range, attenuation, exponent, ambient, specular, texture
  - \\
* - light.type
  - spot, directional
  - point, image
  - \\
* - light.mode
  - fixed, track, targetbody
  - trackcom, targetbodycom
  - \\
```

计划支持的标签：

`flexcomp`, `frame`, `attach`, `contact/pair`, `deformable`

不支持的标签：

`compisite`

### Equality

已支持标签：

```{list-table}
:header-rows: 1
:widths: 25 50 40 20
:class: longtable
* - **标签**
  - **已支持属性**
  - **计划支持属性**
  - **不支持属性**
* - connect
  - active, solref, solimp, body1, body2, anchor, site1, site2
  - \\
  - \\
* - weld
  - active, solref, solimp, body1, body2, relpose, anchor, site1, site2
  - torquescale
  - \\
* - joint
  - active, solref, solimp, joint1, joint2, polycoef
  - \\
  - \\
```

计划支持标签：

`tendon`, `flex`, `distance`

### Tendons

已支持标签：

```{list-table}
:header-rows: 1
:widths: 25 50 40 20
:class: longtable
* - **标签**
  - **已支持属性**
  - **计划支持属性**
  - **不支持属性**
* - fixed
  - limited, range, solreflimit, solimplimit, springlength, stiffness, damping
  - solreffriction, solimpfriction, frictionloss
  - \\

```

计划支持标签：`spatial`

### Actuator

已支持标签：

```{list-table}
:header-rows: 1
:widths: 25 50 40 20
:class: longtable
* - **标签**
  - **已支持属性**
  - **计划支持属性**
  - **不支持属性**
* - general
  - ctrllimited, forcelimited, ctrlrange, forcerange, gear, joint, tendon, gaintype, biastype, dynprm, gainprm, biasprm
  - dyntype, actlimited, actrange, lengthrange, cranklength, jointinparent, site, refsite, body, cranksite, slidersite, actdim, actearly
  - \\
* - general.gaintype
  - fixed,affine
  - muscle
  - user
* - general.biastype
  - none, affine
  - muscle
  - user
* - motor
  - \\
  - \\
  - \\
* - position
  - kp,kv, inheritrange
  - dampratio,timeconst
  - \\
* - velocity
  - kv
  - \\
  - \\

```

计划支持标签：

`intvelocity`, `damper`, `cylinder`, `muscle`, `adhesion`

### Sensors

```{list-table}
:header-rows: 1
:widths: 25 50 40 20
:class: longtable
* - **标签**
  - **已支持属性**
  - **计划支持属性**
  - **不支持属性**
* - accelerometer<br>velocimeter<br>
  - site
  - \\
  - \\
* - jointpos<br>jointvel
  - joint
  - \\
  - \\
* - framepos<br>framequat<br>framexaxis<br>frameyaxis<br>framezaxis
  - objtype, objname, reftype, refname
  - \\
  - \\
* - framelinvel<br>frameangvel
  - objtype, objname
  - \\
  - \\
* - subtreecom<br>subtreelinvel<br>subtreeangmom
  - body
  - \\
  - \\

```

计划支持标签：

`touch`,`force`,`torque`,`magnetometer`,`cameraprojection`,`rangefinder`,
`tendonpos`,`tendonvel`,`actuatorpos`,`actuatorvel`,`actuatorfrc`,
`jointactuatorfrc`,`tendonactuatorfrc`,`ballquat`,`ballangvel`,
`jointlimitpos`,`jointlimitvel`,`jointlimitfrc`,
`tendonlimitpos`,`tendonlimitvel`,`tendonlimitfrc`,`framelinacc`,`frameangacc`,
`distance`,`normal`,`fromto`,`e_potential`,`e_kinetic`,`clock`

```{note}
对于 sensor 中的 objtype 属性，目前支持 body, xbody, geom, site, 不支持 camera
```

### Meta

已支持标签：

```{list-table}
:header-rows: 1
:widths: 25 50 40 20
:class: longtable
* - **标签**
  - **已支持属性**
  - **计划支持属性**
  - **不支持属性**
* - replicate
  - count, sep, offset, euler
  - \\
  - \\
* - include
  - file
  - \\
  - \\
```

```{note}
请您注意，MotrixSim 目前在 meta 标签上处理与 mujoco 存在一些出入。主要包含以下方面：

- `replicate`标签功能目前处于有限支持，如果 replicate 内包含了被 actuator 或者 sensor 引用的 body，将会导致引用错误。
- 无论`include`标签出现在 xml 的什么位置，motroxsim 都会把它放在文件的开头进行处理。 这意味着，如果您在 mjcf 的末尾或中间使用了 include，可能会导致一些对象的遍历顺序发生变化。
```

计划支持标签：

`frame`

### Keyframe

```{list-table}
:header-rows: 1
:widths: 25 50 40 20
:class: longtable
* - **标签**
  - **已支持属性**
  - **计划支持属性**
  - **不支持属性**
* - key
  - time, qpos, qvel, ctrl
  - act, mpos, mquat
  - \\
```

### Default

支持子标签：

`mesh`,`material`,`joint`,`geom`,`site`,`camera`,`light`,`tendon`,`general`,`motor`,
`position`,`velocity`,`equality`

计划支持：

`pair`,,`intvelocity`,`damper`,`cylinder`,`muscle`,`adhesion`

### Visual

已支持标签：

```{list-table}
:header-rows: 1
:widths: 25 50 40 20
:class: longtable
* - **标签**
  - **已支持属性**
  - **计划支持属性**
  - **不支持属性**
* - global
  - orthographic, fovy, azimuth, elevation
  - ipd, linewidth, glow, offwidth, offheight, realtime, ellipsoidinertia, bvactive
  - \\
* - headlight
  - ambient, diffuse, active
  - specular
  - \\
* - map
  - fogstart, fogend, znear, zfar
  - stiffness, stiffnessrot, force, torque, alpha, haze, shadowclip, shadowscale, actuatortendon
  - \\
* - rgba
  - fog
  - haze, force, inertia, joint, actuator, actuatornegative, actuatorpositive, com, camera, light, selectpoint, connect, contactpoint, contactforce, contactfriction, contacttorque, contactgap, rangefinder, constraint, slidercrank, crankbroken, frustum, bv, bvactive
  - \\
```

```{note}
始终会有一个根据 global 配置的自由摄像机作为初始相机。

始终会有头灯和环境光两个光源，且均不产生阴影。
```

计划支持标签：`quality`，`scale`
