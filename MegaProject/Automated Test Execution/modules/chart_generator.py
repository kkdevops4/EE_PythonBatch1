import matplotlib.pyplot as plt


class ChartGenerator:

    @staticmethod
    def generate(
        pass_count,
        fail_count,
        not_executed_count,
        output_file
    ):

        labels = []
        sizes = []

        if pass_count > 0:
            labels.append("Pass")
            sizes.append(pass_count)

        if fail_count > 0:
            labels.append("Fail")
            sizes.append(fail_count)

        if not_executed_count > 0:
            labels.append("Not Executed")
            sizes.append(not_executed_count)

        plt.figure(figsize=(6, 6))

        plt.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%"
        )

        plt.title("BCM Test Execution Summary")

        plt.savefig(output_file)
        plt.close()