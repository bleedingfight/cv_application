import cv2
import argparse
import numpy as np
backends = (cv2.dnn.DNN_BACKEND_DEFAULT, cv2.dnn.DNN_BACKEND_HALIDE, cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE, cv2.dnn.DNN_BACKEND_OPENCV)
targets = (cv2.dnn.DNN_TARGET_CPU, cv2.dnn.DNN_TARGET_OPENCL, cv2.dnn.DNN_TARGET_OPENCL_FP16, cv2.dnn.DNN_TARGET_MYRIAD)

from utils.common import *

def parse_model(model_config):
    fs = cv2.FileStorage(model_config,cv2.FILE_STORAGE_READ)
    model_path = fs.getNode("model")
    config_path = fs.getNode("config")
    label_path = fs.getNode('label')
    model_config = {}
    model_config.update({'model_path':model_path,'config_path':config_path,'label_config':label_path})
    return model_config
def parse_from_cli():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--zoo', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models.yml'),
                        help='An optional path to file with preprocessing parameters.')
    parser.add_argument('--input',
                        help='Path to input image or video file. Skip this argument to capture frames from a camera.')
    parser.add_argument('--framework', choices=['caffe', 'tensorflow', 'torch', 'darknet'],
                        help='Optional name of an origin framework of the model. '
                             'Detect it automatically if it does not set.')
    parser.add_argument('--backend', choices=backends, default=cv2.dnn.DNN_BACKEND_DEFAULT, type=int,
                        help="Choose one of computation backends: "
                             "%d: automatically (by default), "
                             "%d: Halide language (http://halide-lang.org/), "
                             "%d: Intel's Deep Learning Inference Engine (https://software.intel.com/openvino-toolkit), "
                             "%d: OpenCV implementation" % backends)
    parser.add_argument('--target', choices=targets, default=cv2.dnn.DNN_TARGET_CPU, type=int,
                        help='Choose one of target computation devices: '
                             '%d: CPU target (by default), '
                             '%d: OpenCL, '
                             '%d: OpenCL fp16 (half-float precision), '
                             '%d: VPU' % targets)
    args, _ = parser.parse_known_args()
    return args


#
#
#
# add_preproc_args(args.zoo, parser, 'classification')
# parser = argparse.ArgumentParser(parents=[parser],
#                                  description='Use this script to run classification deep learning networks using OpenCV.',
#                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# args = parser.parse_args()
#
# args.model = findFile(args.model)
# args.config = findFile(args.config)
# args.classes = findFile(args.classes)
#
# # Load names of classes
# classes = None
# if args.classes:
#     with open(args.classes, 'rt') as f:
#         classes = f.read().rstrip('\n').split('\n')
#
# # Load a network
# net = cv2.dnn.readNet(args.model, args.config, args.framework)
# net.setPreferableBackend(args.backend)
# net.setPreferableTarget(args.target)
#
# winName = 'Deep learning image classification in OpenCV'
# cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
#
# cap = cv2.VideoCapture(args.input if args.input else 0)
# while cv2.waitKey(1) < 0:
#     hasFrame, frame = cap.read()
#     if not hasFrame:
#         cv2.waitKey()
#         break
#
#     # Create a 4D blob from a frame.
#     inpWidth = args.width if args.width else frame.shape[1]
#     inpHeight = args.height if args.height else frame.shape[0]
#     blob = cv2.dnn.blobFromImage(frame, args.scale, (inpWidth, inpHeight), args.mean, args.rgb, crop=False)
#
#     # Run a model
#     net.setInput(blob)
#     out = net.forward()
#
#     # Get a class with a highest score.
#     out = out.flatten()
#     classId = np.argmax(out)
#     confidence = out[classId]
#
#     # Put efficiency information.
#     t, _ = net.getPerfProfile()
#     label = 'Inference time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency())
#     cv2.putText(frame, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
#
#     # Print predicted class.
#     label = '%s: %.4f' % (classes[classId] if classes else 'Class #%d' % classId, confidence)
#     cv2.putText(frame, label, (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
#
#     cv2.imshow(winName, frame)
