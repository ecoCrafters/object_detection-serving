FROM tensorflow/serving

# Copy the exported model to the container
COPY ./exported_model/my_model/saved_model /models/obj_det/1

# Specify the model base path and the model name
ENV MODEL_BASE_PATH=/models
ENV MODEL_NAME=obj_det

# Expose the default gRPC port
EXPOSE 8501

# Start TensorFlow Serving
CMD tensorflow_model_server --port=8501 --rest_api_port=8502 --model_base_path=${MODEL_BASE_PATH} --model_name=${MODEL_NAME}
