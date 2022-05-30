file_list=( "/home/zaid/project/PrepareData.py" "/home/zaid/project/TrainModel.py" "/home/zaid/project/PrepareSimulationData.py" "/home/zaid/project/IMU_Prediction.py" "/home/zaid/project/PredictionVoting.py" )


for py_file in "${file_list[@]}"
do
    python ${py_file}
done
