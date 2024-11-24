import json

subject_ids = ["sub-3877", "sub-3878", "sub-3879", "sub-3880", "sub-3882", "sub-3883", "sub-3891", "sub-3892", "sub-3903"]

for subject in subject_ids:
  path_to_func_json = subject + f'/func/{subject}_task-rest_run-01_bold.json'

  with open(path_to_func_json, 'r') as file:
    data = json.load(file)

  slice_timing = data.get('SliceTiming')

  if slice_timing is None:
    print(f"Slice timing information not found in the JSON file for {subject}")
  else:
    print(f"Extracting Slice Timing Information for {subject}:")
  
  slice_timing_file = subject + f'/func/{subject}_slice_timing.txt'

  with open(slice_timing_file, 'w') as output_file:
    for value in slice_timing:
      output_file.write(f"{value}\n")

  print(f"Slice timing information saved to {slice_timing_file}")
