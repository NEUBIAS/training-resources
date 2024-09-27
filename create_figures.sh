# Requirements

## Mac
# brew install yq
# brew install --cask libreoffice


# List of modules to exclude
exclude_modules=("tool_installation" "image_inspection_and_presentation")

# Function to check if a module is in the exclude list
is_excluded() {
  local e
  for e in "${exclude_modules[@]}"; do [[ "$e" == "$1" ]] && return 0; done
  return 1
}

# Extract the module_order and execute the command for each, excluding specified modules

i=0
i_max=3 # Set to a low number for development, otherwise set to 99999

yq e '.module_order[]' _config.yml | while read module; do
  if ! is_excluded "$module"; then
    i=$((i+1))
    echo ${i}: ${module}
    #soffice --headless --convert-to png --outdir ./figures figures/resources/"${module}".pptx
  fi
  if [ $i -eq $i_max ]; then
    break
  fi
done
