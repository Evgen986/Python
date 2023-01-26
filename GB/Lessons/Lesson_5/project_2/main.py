from progress.bar import ChargingBar

bar = ChargingBar('Processing', max=20)
for i in range(20):
    # Do some work
    bar.next()
bar.finish()
