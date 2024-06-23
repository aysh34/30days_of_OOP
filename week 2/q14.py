import statistics


class PluginBase:
    def load(self):
        print("\nData Processor Plugin loaded.")

    def unload(self):
        print("\nData Processor Plugin unloaded.")


class DataProcessingMixin:
    def process_data(self, data):
        print("\nData processing....")
        median = statistics.median(data)
        return median


class DataProcessorPlugin(PluginBase, DataProcessingMixin):
    def filter_data(self, data, criteria):
        print("\nFiltering data based on criteria....")
        for i in data:
            if i > criteria:
                filtered_data = [number for number in data if number < criteria]  # list comprehension
                return filtered_data


plugin = DataProcessorPlugin()
plugin.load()
data = [10, 20, 30, 40, 50, 60, 70, 120]
median_value = plugin.process_data(data)
print(f"The median of given data is {median_value}")
filtered_data_list = plugin.filter_data(data, 100)
print(filtered_data_list)
plugin.unload()