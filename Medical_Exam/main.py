import medical_data_visualizer
from unittest import main
import datetime

print("Programmer: Mamoudou T. Bah")
time = datetime.datetime.now()
print(f"Medical Exam Data, {time.strftime('%B %d, %Y @ %H:%M:%S')}")
print("")
# Test your function by calling it here
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run unit tests automatically
main(module='test_module', exit=False)