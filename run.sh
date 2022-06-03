file_list=( "/home/zaid/project/Recognition-of-ADL-s/PrepareData.py" "/home/zaid/project/Recognition-of-ADL-s/TrainModel.py" "//home/zaid/project/Recognition-of-ADL-s/PrepareSimulationData.py" "/home/zaid/project/Recognition-of-ADL-s/IMU_Prediction.py" "/home/zaid/project/Recognition-of-ADL-s/PredictionVoting.py" )


for py_file in "${file_list[@]}"
do
    python ${py_file}
done
