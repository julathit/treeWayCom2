
"use strict";

let drive_motor = require('./drive_motor.js');
let servo_angle = require('./servo_angle.js');
let camera_config = require('./camera_config.js');

module.exports = {
  drive_motor: drive_motor,
  servo_angle: servo_angle,
  camera_config: camera_config,
};
