import pandas as pd
import os
import pickle


class IMU_Prediction():
    Y_labels_reverse = {0: 'Walk', 1: 'OpenDoor', 2: 'CloseDoor', 3: 'BrushTeeth', 4: 'SitDown', 5: 'DrinkGlass',
                        6: 'CleanTable', 7: 'StandUp', 8: 'PourWater'}

    IMU_list = ["lla", "lua", "rla", "rua", "rt", "back"]

    data_path_prefix = r"/home/zaid/project/simulationdata"

    model_path_prefix = r"/home/zaid/project/model"

    prediction_path_prefix = r"/home/zaid/project/IMU_Predication"

    IMU = ""

    def load_model(self):
        with open(os.path.join(self.model_path_prefix, f"{self.IMU}_pkl"), "rb") as m:
            model = pickle.load(m)

        return model

    def load_data(self):
        df = pd.read_csv(os.path.join(self.data_path_prefix, f"{self.IMU}_test_data.csv"))
        return df

if __name__ == "__main__":
    obj = IMU_Prediction()


    for IMU in obj.IMU_list:

        obj.IMU = IMU
        df = obj.load_data()
        model = obj.load_model()
        y_pred = model.predict(df)
        y_pred = [obj.Y_labels_reverse[y] for y in y_pred]
        column_name = f"{obj.IMU}_y_pred"
        pred_df = pd.DataFrame(columns=[column_name])
        pred_df[column_name] = y_pred
        pred_df.to_csv(os.path.join(obj.prediction_path_prefix, f"{obj.IMU}_pred.csv"), index=False)

        print(f"Prediction stored for {obj.IMU} ")


