INPUT_FILE="./sample_1.txt"
NB_LINES=10000000
OUTPUT_FILE="./sample_1_shuffled.txt"
BATCH_SIZE=100000

# Generate random file
echo "Generate random file ${INPUT_FILE} containing ${NB_LINES}"
#generate-random-file --path_file "${INPUT_FILE}" --nb_lines "${NB_LINES}"

# Shuffle the file created
echo "Shuffle the file ${INPUT_FILE} to ${OUTPUT_FILE}"
shuffle-big-file --input_file "${INPUT_FILE}" --batch_size "${BATCH_SIZE}" --output_file "$OUTPUT_FILE"
echo "Done"
