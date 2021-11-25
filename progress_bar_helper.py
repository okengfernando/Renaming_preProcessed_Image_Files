import sys, time

def progressBar(count, total, suffix=''):
    barLength = 60
    filledLength = int(round(barLength * count / float(total)))

    percent = round(100.0 * count / float(total), 0)
    bar = '|' * filledLength + '-' * (barLength - filledLength)


    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percent, '%', suffix))
    sys.stdout.flush()

