# 1. Compacta todos os arquivos da pasta ./plugins/ em um arquivo zip
zip -r ./deployment/plugins-sensedia-msk-connect-optl-analytics.zip ./plugins/*

# 2. Substitui o arquivo zip existente no bucket S3 da AWS (ajuste o nome do bucket conforme necessário)
aws s3 cp ./deployment/plugins-sensedia-msk-connect-optl-analytics.zip s3://343218206630-sensedia-msk-connect-artifactory/msk-optl-analytics/deployment/plugins-sensedia-msk-connect-optl-analytics.zip

# 3. Atualiza o plugin MSK existente na AWS para usar o novo arquivo zip
# Deleta o plugin customizado existente
aws kafkaconnect delete-custom-plugin \
    --custom-plugin-arn arn:aws:kafkaconnect:us-east-1:343218206630:custom-plugin/sensedia-msk-connect-plugin-optl-analytics/62ed8a5b-9582-4cab-b500-c5960e3b7012-3

# Cria um novo plugin customizado apontando para o novo arquivo zip no S3
aws kafkaconnect create-custom-plugin \
    --name sensedia-msk-connect-plugin-optl-analytics \
    --location '{"s3Location":{"bucketArn":"arn:aws:s3:::343218206630-sensedia-msk-connect-artifactory","fileKey":"msk-optl-analytics/deployment/plugins-sensedia-msk-connect-optl-analytics.zip"}}' \
    --content-type ZIP