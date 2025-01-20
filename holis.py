from google.cloud import storage

# Crear cliente de GCS
storage_client = storage.Client()

# Intentar listar los buckets
buckets = list(storage_client.list_buckets())

if buckets:
    print("Conexión exitosa. Buckets encontrados:")
    for bucket in buckets:
        print(bucket.name)
else:
    print("No se encontraron buckets. Revisa las credenciales.")
