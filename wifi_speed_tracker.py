import os
import logging
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates, rcParams

SPEEDTEST_CMD = r'C:\Python\Python37-32\Scripts\speedtest-cli'
LOG_FILE = 'speedtest.log'

def main():
  config_logging()
  for ping_counter in range(30): # Ping the server 30 times
    try:
      ping, download, upload = get_ping_results()
      logging.info("%5.2f %5.2f %5.2f", ping, download, upload)
    except ValueError as err:
      logging.info(err)
  print(read_data())
  create_plot(read_data())
  
def config_logging():
  logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                      format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M",)

def get_ping_results():
  ping = download = upload = None
  
  with os.popen(SPEEDTEST_CMD + ' --simple') as speedtest_output:
    for line in speedtest_output:
      label, value, unit = line.split()
      if 'Ping' in label:
        ping = float(value)
      elif 'Download' in label:
        download = float(value)
      elif 'Upload' in label:
        upload = float(value)

  if all((ping, download, upload)):
    return ping, download, upload
  else:
    raise ValueError('TEST FAILED')

def read_data():
  dataframe = pd.io.parsers.read_csv(LOG_FILE, names='date time ping download upload'.split(),
                              header=None, sep=r'\s+', parse_dates={'timestamp':[0,1]},
                              na_values=['TEST','FAILED'],)

  return dataframe

def create_plot(df):
  plot_file_name = 'bandwidth.png'
  rcParams['xtick.labelsize'] = 'xx-small'

  plt.plot(df['timestamp'], df['download'], 'b-')
  plt.title('1519 W.Taylor St Xfinity Bandwidth Report')
  plt.ylabel('Bandwidth in MBps')
  plt.yticks(range(20, 41))
  plt.ylim(20.0, 40.0)

  plt.xlabel('Date/Time')
  plt.xticks(rotation='45')

  plt.grid()

  current_axes = plt.gca()
  current_figure = plt.gcf()

  hfmt = dates.DateFormatter('%m/%d %H:%M:%S')
  current_axes.xaxis.set_major_formatter(hfmt)
  current_figure.subplots_adjust(bottom=.25)

  loc = current_axes.xaxis.get_major_locator()
  loc.maxticks[dates.HOURLY] = 24
  loc.maxticks[dates.MINUTELY] = 60

  current_figure.savefig(plot_file_name)
  current_figure.show()


if __name__ == '__main__':
  main()
