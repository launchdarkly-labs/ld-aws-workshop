# Getting Started

cd ~/environment && \
git clone https://github.com/jamesbland123/workshop-sample modernization-workshop
cd modernization-workshop
git submodule init
git submodule update

cd ~/environment/modernization-workshop/modules/30_workshop_app

aws cloudformation create-stack --stack-name WorkshopServices --template-body file://services.yaml --capabilities CAPABILITY_NAMED_IAM

sdk-dbfce512-579f-4101-9104-527525a8c8dd
