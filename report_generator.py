import pandas as pd
import os


class ReportGenerator:

    def export_csv(self, completed, missed):

        os.makedirs("outputs", exist_ok=True)

        df = pd.DataFrame(completed + missed)

        df.to_csv("outputs/report.csv", index=False)

        return "outputs/report.csv"

    def export_excel(self, completed, missed):

        path = "outputs/report.xlsx"

        df = pd.DataFrame(completed + missed)

        df.to_excel(path, index=False)

        return path

    def export_txt(self, kpis):

        path = "outputs/report.txt"

        with open(path, "w") as f:

            f.write("TASK SCHEDULER REPORT\n\n")

            for k, v in kpis.items():

                f.write(f"{k}: {v}\n")

        return path