#!/bin/bash

# Function to check if a directory exists
check_VM_exists() {
  if [ -d "$1" ]; then
    return 0 # Directory exists and not equal to "deactivate"
  else
    return 1 # Directory does not exist
  fi
}

env_install() {
  echo "--------Start creating VM folder----------"
  virtualenv VM_system
  echo "--------VM folder is created successful-----"
  echo "--------Start install python libraries -----"
  pip install -r requirements.txt
  echo "--------Install python libraries successful-----"
}

# Check if VM_system directory exists
if [ "$1" = "deactivate" ]; then
  echo "Deactivate VM"
  deactivate
else
  if check_VM_exists "VM_system"; then
    echo "Folder 'VM_system' exists."

    # Change directory to VM_system/Scripts/
    if cd "VM_system/Scripts/"; then
      echo "Changed directory to VM_system/Scripts/."

      # Source the activate script
      if source activate; then
        echo "Virtual environment activated."
      else
        echo "Failed to activate virtual environment."
      fi

      cd ../.. #cd back to root directory
    else
      echo "Failed to change directory to VM_system/Scripts/."
    fi
  else
    echo "Folder 'VM_system' does not exist."
    env_install # Call your env_install function here
  fi

fi
