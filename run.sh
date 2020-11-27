if [ $1 == 'test' ] 
then 
    C:/windows/py.exe test.py 
elif [ $1 == 'build' ]
then
    C:/windows/py.exe setup.py sdist bdist_wheel

    if [ $1 == '-u' ]
    then
        C:/windows/py.exe -m twine upload dist/*
    fi
elif [ $1 == 'upload' ]
then
    C:/windows/py.exe -m twine upload dist/*
elif [ $1 == 'commit' ]
then
    echo "Commit Description: "
    read commitln

    git add .
    git commit -m \"$commitln\"
    git push github
else
    echo "Command not found!"
fi