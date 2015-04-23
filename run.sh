let var3=10
var3=$(python image_process.py)
let var3=var3-1
var=$(gsettings get com.canonical.Unity.Launcher favorites)
let counter=-1
declare -a ARRAY
const1=0
for i in $var; do
	if [ ${#i} -gt 23 ]; then
		let counter=counter+1
		var2=${#i}
		let var2=var2-17
		#echo $var2
		if [ $counter -eq $const1 ]; then
			let var2=var2-1
			ARRAY[$counter]=${i:16:var2}
		else
			ARRAY[$counter]=${i:15:var2}
		fi
	else
		sleep 0;
	fi	
done 
cd /
echo $var3
echo ${ARRAY[var3]}
`grep '^Exec' /usr/share/applications/${ARRAY[var3]} | tail -1 | sed 's/^Exec=//' | sed 's/%.//'` & 
#echo $var
