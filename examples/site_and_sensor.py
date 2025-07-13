# Copyright (C) 2020-2025 Motphys Technology Co., Ltd. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import time

import numpy as np

from motrixsim import SceneData, load_model, step
from motrixsim.render import RenderApp


# Mouse controls:
# - Press and hold left button then drag to rotate the camera/view
# - Press and hold right button then drag to pan/translate the view
def main():
    # Create render window for visualization
    render = RenderApp()
    # The scene description file
    path = "examples/assets/site_and_sensor.xml"
    # Load the scene model
    model = load_model(path)
    # Create the render instance of the model
    render.launch(model)
    # Create the physics data of the model
    data = SceneData(model)

    # tag::site_access[]
    # ----------Try to access site----------
    # How many sites are in the model?
    num_sites = model.num_sites
    # Site objects
    sites = model.sites
    # Site names
    site_names = model.site_names
    print(f"num_sites : {num_sites}, sites : {sites}, site_names : {site_names}")

    # Get site by name
    car_imu = model.get_site("car_imu")
    # The index of the site
    index = car_imu.parent_link_index
    print(f"car_imu index : {index}")
    # Which link is the site attached?
    link_name = car_imu.parent_link
    print(f"The car_imu site is on : [{link_name}] link")
    # Site name
    site_name = car_imu.name
    print(f"site_name of car_imu : {site_name}")
    # The site position
    pos = car_imu.pos
    # The site rotation
    quat = car_imu.quat
    print(f"car_imu's position : {pos}, car_imu's rotation : {quat}")
    # ----------End----------
    # end::site_access[]
    # How many sensors are in the model?
    num_sensors = model.num_sensors
    print(f"num_sensors : {num_sensors}")

    # Set slide actuator control
    act = model.get_actuator("actuator_slider")
    act.set_ctrl(data, 1.0)

    # Set hinge joint velocity
    hinge = model.get_joint("hinge")
    hinge.set_dof_vel(data, np.array([15]))

    # Wait for creating render world
    time.sleep(1.5)

    while True:
        # Control the step interval to prevent too fast simulation
        time.sleep(0.02)
        # Physics world step
        step(model, data)

        # tag::get_sensor_value[]
        # Get sensor value directly
        v0 = model.get_sensor_value("vel_0", data)
        v1 = model.get_sensor_value("vel_1", data)
        v2 = model.get_sensor_value("vel_2", data)
        v3 = model.get_sensor_value("vel_3", data)
        print(f"velocimeter values are : {v0}, {v1}, {v2}, {v3}")

        acc_0 = model.get_sensor_value("acc_0", data)
        acc_1 = model.get_sensor_value("acc_1", data)
        acc_2 = model.get_sensor_value("acc_2", data)
        acc_3 = model.get_sensor_value("acc_3", data)
        print(f"accelerometer values are : {acc_0}, {acc_1}, {acc_2}, {acc_3}")

        gyro_0 = model.get_sensor_value("gyro_0", data)
        gyro_1 = model.get_sensor_value("gyro_1", data)
        gyro_2 = model.get_sensor_value("gyro_2", data)
        gyro_3 = model.get_sensor_value("gyro_3", data)
        print(f"gyro values are : {gyro_0}, {gyro_1}, {gyro_2}, {gyro_3}")
        # end::get_sensor_value[]

        print("-----------------------------------------")

        # tag::get_sensor_values[]
        sensor_values = model.get_sensor_values(data)
        print(f"all sensor values are : {sensor_values}")
        # end::get_sensor_values[]
        print("-----------------------------------------")

        # Sync render objects from physic world
        render.sync(data)


if __name__ == "__main__":
    main()
