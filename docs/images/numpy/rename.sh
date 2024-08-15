for file in *; do
  # Check if the file name contains a hyphen
  if [[ "$file" == *-* ]]; then
    # Replace hyphens with underscores in the file name
    new_file="${file//-/_}"
    # Rename the file
    mv "$file" "$new_file"
  fi
done

echo "Renaming completed."
