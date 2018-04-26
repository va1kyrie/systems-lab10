# LAB 11
Helen Dougherty & Robert Neubauer

## Average Daily Power Budget for 6 months
(365 days/2) * 24 hours/day = 4380 hours

(350/4380) = .08mA/hr => 1.92mA/day

(210/4380) = .048mA/hr => 1.152mA/day
## Measuring System Current
- Total (thru battery): 102 mA
- Lora Module: ~50 mA
- Nucleo: ~52 mA


- All other components have negligible amounts of current running through them, on the order of 0.02 mA or 0.05 mA.

## Low Power mode
The overall current through the system is about 20 mA with the Nucleo using sleep() and the Lora module using its sleep mode.

## Estimated Run Time
With a normal capacitance of 350 mAh on the battery, our current system will run for roughly 17.5 hours. In cold temperatures, with a capacitance of 210 mAh, it will run approximately 10.5 hours. In hot temperatures, with a capacitance of 280 mAh, it will run approximately 14 hours.

## Report
Our system currently does not meet the 6 month requirement. There are a number of possible approaches to meet this requirement:

- **Increase the power supply**. By using a battery with a larger capacitance, an alternate power supply such as solar, or a combination, the increased draw might be mitigated.
- **Use deep sleep mode or stop mode**. By using a deeper sleep mode, a stop mode/hibernation mode, or similar, we could decrease the power used by drawing as little power as possible between measurements and transmissions.
- **Decrease the payload size of the transmissions**. Reduce both the number of transmissions needed and the size of the information transmitted. This will reduce the active time of the Lora module, which is one of the main power draws.
- **Decrease number of measurements taken**. By reducing the number of measurements taken (every 2 hours, for example, instead of every hour), the information over 24 hours will be reduced, decreasing the information to be transmitted each day and/or allowing transmissions to occur every 48 hours instead of every day. This would, again, reduce the active time of the Lora module and reduce the active time of the entire system.
