rm -frv temp.log
echo "$(date)" >> temp.log
sum="$(crc32 temp.log)"

precommit=$sum
commitmsg="$1"

rm -frv temp.log

git add .
git commit -m "${precommit} | ${commitmsg}"
git push
