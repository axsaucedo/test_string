
build_images:
	cd step_one && ./build_image.sh
	cd step_two && ./build_image.sh

send_request: 
	curl -X POST -H 'Content-Type: application/json' \
		-d "{'data': {'names': [], 'ndarray': ['hello world', 'this is another']}}" \
		http://localhost:31707/seldon/default/text-example/api/v0.1/predictions

