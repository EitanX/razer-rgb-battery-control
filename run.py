import openrazer.client

dm = openrazer.client.DeviceManager()
dock = dm.devices[0]
mouse = dm.devices[1]

pct = mouse.battery_level / 100

if pct < 0.15:
    col = (255, 0, 0)
else:
    pct_diff = 1.0 - pct
    red = min(255, pct_diff * 2 * 255)
    green = min(255, pct * 2 * 255)
    col = (int(red), int(green), 0)

dock.fx.static(*col)
mouse.fx.static(*col)
