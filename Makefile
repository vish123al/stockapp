test:	
	@ echo "Pulling latest images..."
	@ docker pull vishaldenge/stocknew
	@ echo "Building images..."
	@ docker build  -t vishaldenge/stocknew .
	@ echo "Ensuring image is ready"
	@ docker ps
	@ echo "login checking"
	@ docker login -u admin -p 'password'
	@ echo "testing image for push"
	@ docker push vishaldenge/stocknew 
	@ echo "Testing complete"
