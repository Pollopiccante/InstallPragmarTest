
# build package wheel, and use it while building container
echo "BUILD PACKAGE WHEEL"
cd .. && python3 -m build
echo "BUILD DOCKER CONTAINER TO TEST"
docker build -f InstallPragmarTest/Test.Dockerfile -t 'pragmar_test_container' .

echo "CLEAR WHEEL FILES"
cd dist && rm ./*

echo "RUN TEST CONTAINER"
if docker run pragmar_test_container:latest; then
  echo "ALL TESTS PASSED"
else
  echo "TESTS FAILED"
  exit 1
fi

echo "CLEAR DOCKER ARTIFACTS"
docker rm -f $(docker ps -a -q --filter ancestor=pragmar_test_container)