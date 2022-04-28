export BRANCH_NAME=$1
git init
git remote add origin https://gl.infratest.livibank.hk/julian.yip/ml_toolkit.git
git branch $BRANCH_NAME
git branch -M $BRANCH_NAME
git add .
git commit -m "$2"
git push -u origin $BRANCH_NAME