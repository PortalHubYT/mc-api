# fetch server.jar
python3 src/fetch_jar.py

# parse server.jar
java -cp server.jar net.minecraft.data.Main --server --reports

# clean
rm -rf logs
rm -rf server.jar


