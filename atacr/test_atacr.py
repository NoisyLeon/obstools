# import surfpy.atacr.classes as classes
# 
# daynoise = classes.DayNoise('demo')


from obstools.atacr import DayNoise, TFNoise, EventStream
daynoise = DayNoise('demo')
# Uploading demo data - March 04, 2012, station 7D.M08A
daynoise.QC_daily_spectra()
daynoise.average_daily_spectra()
tfnoise_day = TFNoise(daynoise)
tfnoise_day.transfer_func()
evstream = EventStream('demo')
# Uploading demo earthquake data - March 09, 2012, station 7D.M08A
evstream.correct_data(tfnoise_day)

