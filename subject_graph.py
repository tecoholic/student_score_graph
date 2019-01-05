import sys
import csv

import matplotlib.pyplot as plot


def generate(filename):
    average = None
    subjects = ['Tamil', 'English', 'Maths', 'Science', 'Social']

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row['Name'] == 'Average':
                average = [row['Tamil'], row['English'], row['Maths'], row['Science'], row['Social']]
                continue
            # set the canvas
            canvas = plot.figure()
            rect = canvas.patch
            rect.set_facecolor('white')

            # Set the line markers and other stuff
            plot.xticks([0, 1, 2, 3, 4], subjects)

            marks = [row['Tamil'], row['English'], row['Maths'], row['Science'], row['Social']]
            plot.plot(marks, label=row["Name"], linewidth=2.0)
            plot.plot(average, "r--", label="Class Average")
            plot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
            plot.ylabel("Marks")
            plot.grid(alpha=0.8)
            for x, y in zip([0, 1, 2, 3, 4], marks):
                plot.annotate(y, [x, y], xytext=[-20, 10], textcoords='offset pixels', bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.5))

            for x, y in zip([0, 1, 2, 3, 4], average):
                plot.annotate(y, [x, y], xytext=[0, -20], textcoords='offset pixels', bbox=dict(boxstyle='round,pad=0.2', fc='red', alpha=0.5))
            plot.savefig("{}.png".format(row['Name'].replace(' ', '_')))
            plot.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Run: python generate.py <csv_file>")

    generate(sys.argv[1])
