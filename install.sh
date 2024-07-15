username=`whoami`

pip install -r requirements.txt

rm -rf /home/$username/.forbes_qotd 
mkdir /home/$username/.forbes_qotd

cp -r resources /home/$username/.forbes_qotd/
cp main.py /home/$username/.forbes_qotd/

echo "Finished Installation"
echo -e "Make sure that you have 'Python3' installed\n"
echo -e "1. Now open 'Startup Applications' and add\n"
echo -e "2. 'Forbes QOTD' in the 'Name' section\n"
echo -e "3. 'python3 /home/$username/.forbes_qotd/main.py' in the 'Command' section and save it"
echo -e "\nReboot to see the results!"