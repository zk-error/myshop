import redis
from django.conf import settings
from .models import Product

# conectamos a redis con las instancias definidas en stings
r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)

class Recommender:
    def get_product_key(self, id):
        return f'product:{id}:purchased_with'

    def products_bought(self, product_ids):
        #product_ids = [p.id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:
                # obtener los otros productos comprados con cada producto
                if product_id != with_id:
                    # incrementar la puntuación para el producto comprado junto
                    r.zincrby(self.get_product_key(product_id),1,with_id)

    def suggest_products_for(self, products, max_results=6):
        product_ids = [p.id for p in products]
        if len(products) == 1:
            # solo 1 producto
            suggestions = r.zrange(self.get_product_key(product_ids[0]),0, -1, desc=True)[:max_results]
        else:
            # generar una clave temporal
            flat_ids = ''.join([str(id) for id in product_ids])
            tmp_key = f'tmp_{flat_ids}'
            # múltiples productos, combinar las puntuaciones de todos los productos
            # almacenar el conjunto ordenado resultante en una clave temporal
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(tmp_key, keys)
            # eliminar las IDs de los productos para los que es la recomendación
            r.zrem(tmp_key, *product_ids)
            # obtener las IDs de los productos según su puntuación, orden descendente
            suggestions = r.zrange(tmp_key, 0, -1,desc=True)[:max_results]
            # eliminar la clave temporal
            r.delete(tmp_key)
        suggested_products_ids = [int(id) for id in suggestions]
        # obtener los productos sugeridos y ordenarlos según el orden de aparición
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x: suggested_products_ids.index(x.id))
        return suggested_products

    def clear_purchases(self):
        for id in Product.objects.values_list('id', flat=True):
            r.delete(self.get_product_key(id))





