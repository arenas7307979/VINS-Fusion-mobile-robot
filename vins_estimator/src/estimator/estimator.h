/*******************************************************
 * Copyright (C) 2019, Aerial Robotics Group, Hong Kong University of Science and Technology
 * 
 * This file is part of VINS.
 * 
 * Licensed under the GNU General Public License v3.0;
 * you may not use this file except in compliance with the License.
 *******************************************************/

#pragma once
 
#include <thread>
#include <mutex>
#include <std_msgs/Header.h>
#include <std_msgs/Float32.h>
#include <ceres/ceres.h>
#include <unordered_map>
#include <queue>
#include <opencv2/core/eigen.hpp>
#include <eigen3/Eigen/Dense>
#include <eigen3/Eigen/Geometry>

#include "parameters.h"
#include "feature_manager.h"
#include "../utility/utility.h"
#include "../utility/tic_toc.h"
#include "../initial/solve_5pts.h"
#include "../initial/initial_sfm.h"
#include "../initial/initial_alignment.h"
#include "../initial/initial_ex_rotation.h"
#include "../factor/imu_factor.h"
#include "../factor/initial_pose_factor.h"
#include "../factor/pose_local_parameterization.h"
#include "../factor/marginalization_factor.h"
#include "../factor/projectionTwoFrameOneCamFactor.h"
#include "../factor/projectionTwoFrameTwoCamFactor.h"
#include "../factor/projectionOneFrameTwoCamFactor.h"
#include "../featureTracker/feature_tracker.h"


class Estimator
{
  public:
    Estimator();
<<<<<<< HEAD
=======
    ~Estimator();
>>>>>>> update function

    void setParameter();

    // interface
    void initFirstPose(Eigen::Vector3d p, Eigen::Matrix3d r);
    void inputIMU(double t, const Vector3d &linearAcceleration, const Vector3d &angularVelocity);
    void inputFeature(double t, const map<int, vector<pair<int, Eigen::Matrix<double, 7, 1>>>> &featureFrame);
    void inputImage(double t, const cv::Mat &_img, const cv::Mat &_img1 = cv::Mat());
    void processIMU(double t, double dt, const Vector3d &linear_acceleration, const Vector3d &angular_velocity);
    void processImage(const map<int, vector<pair<int, Eigen::Matrix<double, 7, 1>>>> &image, const double header);
    void processMeasurements();

    // internal
    void clearState();
    bool initialStructure();
    bool visualInitialAlign();
    bool relativePose(Matrix3d &relative_R, Vector3d &relative_T, int &l);
    void slideWindow();
    void slideWindowNew();
    void slideWindowOld();
    void optimization();
    void vector2double();
    void double2vector();
    bool failureDetection();
    bool getIMUInterval(double t0, double t1, vector<pair<double, Eigen::Vector3d>> &accVector, 
                                              vector<pair<double, Eigen::Vector3d>> &gyrVector);
    void getPoseInWorldFrame(Eigen::Matrix4d &T);
    void getPoseInWorldFrame(int index, Eigen::Matrix4d &T);
    void predictPtsInNextFrame();
    void outliersRejection(set<int> &removeIndex);
    double reprojectionError(Matrix3d &Ri, Vector3d &Pi, Matrix3d &rici, Vector3d &tici,
                                     Matrix3d &Rj, Vector3d &Pj, Matrix3d &ricj, Vector3d &ticj, 
                                     double depth, Vector3d &uvi, Vector3d &uvj);
    void updateLatestStates();
    void fastPredictIMU(double t, Eigen::Vector3d linear_acceleration, Eigen::Vector3d angular_velocity);
    bool IMUAvailable(double t);
    void initFirstIMUPose(vector<pair<double, Eigen::Vector3d>> &accVector);

    enum SolverFlag
    {
        INITIAL,
        NON_LINEAR
    };

    enum MarginalizationFlag
    {
        MARGIN_OLD = 0,
        MARGIN_SECOND_NEW = 1
    };
<<<<<<< HEAD

=======
    
    std::mutex mProcess; //增加了过程锁
>>>>>>> update function
    std::mutex mBuf;
    queue<pair<double, Eigen::Vector3d>> accBuf;
    queue<pair<double, Eigen::Vector3d>> gyrBuf;
    queue<pair<double, map<int, vector<pair<int, Eigen::Matrix<double, 7, 1> > > > > > featureBuf;
    double prevTime, curTime;
    bool openExEstimation;

    std::thread trackThread;
    std::thread processThread;

    FeatureTracker featureTracker;

    SolverFlag solver_flag;   // VINS-Fusion 系统的状态
    MarginalizationFlag  marginalization_flag;
    Vector3d g;
    // camera与IMU的外参
    Matrix3d ric[2]; // 从相机到IMU的旋转
    Vector3d tic[2]; // 从相机到IMU的平移

    Vector3d        Ps[(WINDOW_SIZE + 1)]; // 滑动窗口中各帧在世界坐标系下的位置
    Vector3d        Vs[(WINDOW_SIZE + 1)];  // 滑动窗口中各帧在世界坐标系下的速度
    Matrix3d        Rs[(WINDOW_SIZE + 1)]; // 滑动窗口中各帧在世界坐标系下的旋转
    Vector3d        Bas[(WINDOW_SIZE + 1)]; // 滑动窗口中各帧对应的加速度计偏置
    Vector3d        Bgs[(WINDOW_SIZE + 1)]; // 滑动窗口中各帧对应的陀螺仪偏置
    double td;  // camera数据与IMU数据时间戳的偏移值

    Matrix3d back_R0, last_R, last_R0;
    Vector3d back_P0, last_P, last_P0;
    double Headers[(WINDOW_SIZE + 1)];

    IntegrationBase *pre_integrations[(WINDOW_SIZE + 1)]; // 滑动窗口中每帧图像对应一个IntegrationBase对象
    Vector3d acc_0, gyr_0;  // 最近一次接收到的IMU数据

     // 滑动窗口中每一帧图像对应的预积分所用到的IMU数据存在3个缓存中
    vector<double> dt_buf[(WINDOW_SIZE + 1)];  // IMU数据对应的时间间隔
    vector<Vector3d> linear_acceleration_buf[(WINDOW_SIZE + 1)]; // IMU加速度计对应的数据（测量值）
    vector<Vector3d> angular_velocity_buf[(WINDOW_SIZE + 1)]; // IMU陀螺仪对应的数据（测量值）

    int frame_count; // 最新帧在滑动窗口中的索引（0，1，2，... ，WINDOW_SIZE）
    int sum_of_outlier, sum_of_back, sum_of_front, sum_of_invalid;
    int inputImageCnt;

    FeatureManager f_manager; // 用于管理滑动窗口对应的特征点数据
    MotionEstimator m_estimator;
    InitialEXRotation initial_ex_rotation;

    bool first_imu;
    bool is_valid, is_key;
    bool failure_occur;

    vector<Vector3d> point_cloud;
    vector<Vector3d> margin_cloud;
    vector<Vector3d> key_poses;
    double initial_timestamp;  // VINS系统完成初始化操作时对应的图像帧的时间戳（需要注意的是，虽然完成了初始化操作，但是初始化不一定成功）

   // 用于ceres优化的参数块
    double para_Pose[WINDOW_SIZE + 1][SIZE_POSE];
    double para_SpeedBias[WINDOW_SIZE + 1][SIZE_SPEEDBIAS];
    double para_Feature[NUM_OF_F][SIZE_FEATURE];
    double para_Ex_Pose[2][SIZE_POSE];
    double para_Retrive_Pose[SIZE_POSE];
    double para_Td[1][1];
    double para_Tr[1][1];

    int loop_window_index;

    MarginalizationInfo *last_marginalization_info;
    vector<double *> last_marginalization_parameter_blocks;

     // 存储所有的ImageFrame对象（每读取一帧图像就会构建ImageFrame对象）
    // 键是图像帧的时间戳，值是ImageFrame对象，ImageFrame对象中保存了图像帧的位姿，相应的预积分和图像特征点信息
    map<double, ImageFrame> all_image_frame;
    IntegrationBase *tmp_pre_integration;   // 用于在创建ImageFrame对象时，把该指针赋给imageframe.pre_integration

    bool margin_init_pose;
    Eigen::Vector3d initP;
    Eigen::Matrix3d initR;

    double latest_time;
    Eigen::Vector3d latest_P, latest_V, latest_Ba, latest_Bg, latest_acc_0, latest_gyr_0;
    Eigen::Quaterniond latest_Q;

    bool initFirstPoseFlag;
<<<<<<< HEAD
=======
    bool initThreadFlag;
>>>>>>> update function
};
