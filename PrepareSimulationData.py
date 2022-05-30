import pandas as pd
import os
import json
from sklearn.preprocessing import StandardScaler
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class PrepareSimulationData():

    IMU = ""

    data_path_prefix = r"/home/zaid/project/output"
    output_data_prefix = r"/home/zaid/project/simulationdata"
    simulated_action_sequnce = ""
    IMU_list = ["lla", "lua", "rla", "rua", "rt", "back"]

    def load_simulation_seq(self):

        with open('ADL_Simulation_Sequence.json', 'r') as f:
            self.simulated_action_sequnce = json.load(f)

    def read_data(self):

        df = pd.read_csv(os.path.join(self.data_path_prefix, "test_data.csv"))
        df = df[df["module"] == self.IMU]
        df.drop(labels = ["index", "module"], axis = 1, inplace=True)
        return df

    def prepare_simulated_data(self, df):

        simulation_df = pd.DataFrame()

        for ADL in self.simulated_action_sequnce.keys():

            imu_df = df[df["ADL"] == ADL]
            imu_df = imu_df.iloc[:self.simulated_action_sequnce[ADL]]

            if len(imu_df) != self.simulated_action_sequnce[ADL]:

                remaining_rows = int(self.simulated_action_sequnce[ADL]) - len(imu_df)
                garbage_data = [0]*11
                garbage_data =  [garbage_data] * remaining_rows
                temp_df = pd.DataFrame(garbage_data, columns = imu_df.columns)
                imu_df = imu_df.append(temp_df)

            simulation_df = simulation_df.append(imu_df)

        simulation_df.drop(labels = ["ADL"], axis = 1, inplace=True)

        return simulation_df

        # standardize data

    def preprocess_data(self, X):

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X)
        X_scaled = pd.DataFrame(X_train_scaled, columns=X.columns)
        return X_scaled

if __name__ == "__main__":


    obj = PrepareSimulationData()
    obj.load_simulation_seq()

    for IMU in obj.IMU_list:
        print(IMU)
        obj.IMU  = IMU
        df = obj.read_data()
        test_df = obj.prepare_simulated_data(df)
        test_df = obj.preprocess_data(test_df)
        test_df.to_csv(os.path.join(obj.output_data_prefix, f"{obj.IMU}_test_data.csv"), index=False)
        print(f"Simulation data has been stored for IMU {obj.IMU}")

