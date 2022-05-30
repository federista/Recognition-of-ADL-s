import pandas as pd
import os.path
import os
import json
from sklearn.metrics import accuracy_score

class PredictionVoting():


    simulation_result_path = r"/home/zaid/project/IMU_Predication"
    output_path = r"/home/zaid/project/output"

    simulated_action_sequnce = ""

    IMU_list = ["lla", "lua", "rla", "rua", "rt", "back"]

    def load_simulation_seq(self):

        with open('ADL_Simulation_Sequence.json', 'r') as f:
            self.simulated_action_sequnce = json.load(f)

    def true_labels(self):
        y_true = []

        for ADL in self.simulated_action_sequnce.keys():
            temp_list = [ADL] * int(self.simulated_action_sequnce[ADL])
            y_true.extend(temp_list)
        return y_true

if __name__ == "__main__":

    obj = PredictionVoting()
    obj.load_simulation_seq()
    y_true = obj.true_labels()



    while(True):
        if os.path.exists(os.path.join(obj.simulation_result_path, "lla_pred.csv")) and\
                os.path.exists(os.path.join(obj.simulation_result_path, "lua_pred.csv")) and\
                os.path.exists(os.path.join(obj.simulation_result_path, "rla_pred.csv")) and\
                os.path.exists(os.path.join(obj.simulation_result_path, "rua_pred.csv")) and \
                os.path.exists(os.path.join(obj.simulation_result_path, "back_pred.csv")) and \
                os.path.exists(os.path.join(obj.simulation_result_path, "rt_pred.csv")):
            break

    y_pred = pd.DataFrame()
    for IMU in obj.IMU_list:
        imu_df = pd.read_csv (os.path.join(obj.simulation_result_path, f"{IMU}_pred.csv" ))
        y_pred =  pd.concat([y_pred,imu_df ], axis=1)

    y_pred['majority'] = y_pred.mode(axis=1)[0]
    print(f" voting output \n {y_pred.head(5)}\n")
    y_pred = y_pred['majority']

    accuracy_score = accuracy_score(y_true, y_pred)
    final_df = pd.DataFrame( list(zip(y_true, y_pred)), columns = ["True", "Predicted"])
    final_df.to_csv(os.path.join(obj.output_path, "final_output.csv"), index = False)
    print(f"final output \n{final_df.head(50)}\n")
    print(f"Accuracy : {accuracy_score}")
