# --------------------------------------- Registro de productos Grifería -----------------------------------------
#----------------Perfiles--------------
@app.post('/Add_Perfil')
def Add_Perfil():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Perfil'], new_filename))
                return os.path.join(app.config['IMGS_GF_Perfil'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')

    
    nuevo_perfil = models.Perfil(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_perfil)
    db_session.commit()
    return redirect("perfiles")

@app.post('/Act_Perfil/<id>')
def Act_Perfil(id):
    perfil_act = db_session.query(models.Perfil).get(id)
       
    if perfil_act == None:
        flash('ID no encontrado')
        return redirect (url_for('perfiles'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act'] 
       
    if perfil_act == None:
        flash('No hay nada')
        return redirect (url_for('perfiles'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Perfil'], new_filename))
                return os.path.join(app.config['IMGS_GF_Perfil'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    perfil_act.Imagen = update_image('Imagen_act', perfil_act.Imagen)
    perfil_act.IMG2 = update_image('IMG2_act', perfil_act.IMG2)
    
    perfil_act.Nombre = Name_act
    perfil_act.Precio = Prec_act
    perfil_act.Codigo = Cod_act
    perfil_act.Marca = Marc_act
    perfil_act.Color = Col_act
    perfil_act.Medida = Med_act
       
    db_session.add(perfil_act)
    db_session.commit()
       
    return redirect(url_for('perfiles'))

@app.get('/E_Perfil/<id>')
def E_Perfil(id):
   perfil = db_session.query(models.Perfil).get(id)
   
   if perfil == None:
       flash('ID no encontrado')
       return redirect(url_for('perfiles'))
   
   image_paths = [perfil.Imagen, perfil.IMG2]
    
   base_path = 'static/imagenes/Griferia/Perfiles'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(perfil)
   db_session.commit()
   
   return redirect(url_for('perfiles'))  

#---------------- Cenefas --------------
@app.post('/Add_Cenefa')
def Add_Cenefa():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Cenefa'], new_filename))
                return os.path.join(app.config['IMGS_GF_Cenefa'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_cenefa = models.Cenefa(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_cenefa)
    db_session.commit()
    return redirect("Cenefas")

@app.post('/Act_Cenefa/<id>')
def Act_Cenefa(id):
    cenefa_act = db_session.query(models.Cenefa).get(id)
       
    if cenefa_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cenefas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    
    if cenefa_act == None:
        flash('No hay nada')
        return redirect (url_for('Cenefas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Cenefa'], new_filename))
                return os.path.join(app.config['IMGS_GF_Cenefa'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    cenefa_act.Imagen = update_image('Imagen_act', cenefa_act.Imagen)
    cenefa_act.IMG2 = update_image('IMG2_act', cenefa_act.IMG2)
       
    cenefa_act.Nombre = Name_act
    cenefa_act.Precio = Prec_act
    cenefa_act.Codigo = Cod_act
    cenefa_act.Marca = Marc_act
    cenefa_act.Color = Col_act
    cenefa_act.Medida = Med_act
    cenefa_act.Material = Mat_act
       
    db_session.add(cenefa_act)
    db_session.commit()
       
    return redirect(url_for('Cenefas'))

@app.get('/E_Cenefa/<id>')
def E_Cenefa(id):
   cenefa = db_session.query(models.Cenefa).get(id)
   
   if cenefa == None:
       flash('ID no encontrado')
       return redirect(url_for('Cenefas'))
   
   image_paths = [cenefa.Imagen, cenefa.IMG2]
   base_path = 'static/imagenes/Griferia/Cenefas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(cenefa)
   db_session.commit()
   
   return redirect(url_for('Cenefas'))  

#---------------- Mallas --------------
@app.post('/Add_Malla')
def Add_Malla():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Malla'], new_filename))
                return os.path.join(app.config['IMGS_GF_Malla'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_malla = models.Maya(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_malla)
    db_session.commit()
    return redirect("Mallas")

@app.post('/Act_Malla/<id>')
def Act_Malla(id):
    malla_act = db_session.query(models.Maya).get(id)
       
    if malla_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Mallas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    
    if malla_act == None:
        flash('No hay nada')
        return redirect (url_for('Mallas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Malla'], new_filename))
                return os.path.join(app.config['IMGS_GF_Malla'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    malla_act.Imagen = update_image('Imagen_act', malla_act.Imagen)
    malla_act.IMG2 = update_image('IMG2_act', malla_act.IMG2)
    
    malla_act.Nombre = Name_act
    malla_act.Precio = Prec_act
    malla_act.Codigo = Cod_act
    malla_act.Marca = Marc_act
    malla_act.Color = Col_act
    malla_act.Medida = Med_act
    malla_act.Material = Mat_act
       
    db_session.add(malla_act)
    db_session.commit()
       
    return redirect(url_for('Mallas'))

@app.get('/E_Malla/<id>')
def E_Malla(id):
   malla = db_session.query(models.Maya).get(id)
   
   if malla == None:
       flash('ID no encontrado')
       return redirect(url_for('Mallas'))
   
   image_paths = [malla.Imagen, malla.IMG2]
    
   base_path = 'static/imagenes/Griferia/Mallas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(malla)
   db_session.commit()
   
   return redirect(url_for('Mallas'))  

#---------------- Manerales --------------
@app.post('/Add_Maneral')
def Add_Maneral():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Tip_inst = request.form['Tipo_install']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Maneral'], new_filename))
                return os.path.join(app.config['IMGS_GF_Maneral'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_maneral = models.Maneral(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Tipo_install = Tip_inst,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_maneral)
    db_session.commit()
    return redirect("Manerales")

@app.post('/Act_Maneral/<id>')
def Act_Maneral(id):
    maneral_act = db_session.query(models.Maneral).get(id)
       
    if maneral_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Manerales'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Tip_inst_act = request.form['Tipo_install_act']
    
    if maneral_act == None:
        flash('No hay nada')
        return redirect (url_for('Manerales'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Maneral'], new_filename))
                return os.path.join(app.config['IMGS_GF_Maneral'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    maneral_act.Imagen = update_image('Imagen_act', maneral_act.Imagen)
    maneral_act.IMG2 = update_image('IMG2_act', maneral_act.IMG2)
       
    maneral_act.Nombre = Name_act
    maneral_act.Precio = Prec_act
    maneral_act.Codigo = Cod_act
    maneral_act.Marca = Marc_act
    maneral_act.Color = Col_act
    maneral_act.Material = Mat_act
    maneral_act.Tipo_install = Tip_inst_act
       
    db_session.add(maneral_act)
    db_session.commit()
       
    return redirect(url_for('Manerales'))

@app.get('/E_Maneral/<id>')
def E_Maneral(id):
   maneral = db_session.query(models.Maneral).get(id)
   
   if maneral == None:
       flash('ID no encontrado')
       return redirect(url_for('Manerales'))
   
   image_paths = [maneral.Imagen, maneral.IMG2]
    
   base_path = 'static/imagenes/Griferia/Manerales'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(maneral)
   db_session.commit()
   
   return redirect(url_for('Manerales'))  

#---------------- Regaderas --------------
@app.post('/Add_Regadera')
def Add_Regadera():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Flu = request.form['Flujo_agua']
    Presion = request.form['Presion']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Regadera'], new_filename))
                return os.path.join(app.config['IMGS_GF_Regadera'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_regadera = models.Regadera(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Flujo_agua =Flu,
        Presion =Presion,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_regadera)
    db_session.commit()
    return redirect("Regaderas")

@app.post('/Act_Regadera/<id>')
def Act_Regadera(id):
    regadera_act = db_session.query(models.Regadera).get(id)
       
    if regadera_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Regaderas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Flu_act = request.form['Flujo_agua_act']
    Presi_act = request.form['Presion_act']
    
    if regadera_act == None:
        flash('No hay nada')
        return redirect (url_for('Regaderas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Regadera'], new_filename))
                return os.path.join(app.config['IMGS_GF_Regadera'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    regadera_act.Imagen = update_image('Imagen_act', regadera_act.Imagen)
    regadera_act.IMG2 = update_image('IMG2_act', regadera_act.IMG2)
       
    regadera_act.Nombre = Name_act
    regadera_act.Precio = Prec_act
    regadera_act.Codigo = Cod_act
    regadera_act.Marca = Marc_act
    regadera_act.Color = Col_act
    regadera_act.Medida = Med_act
    regadera_act.Material = Mat_act
    regadera_act.Flujo_agua = Flu_act
    regadera_act.Presion = Presi_act
       
    db_session.add(regadera_act)
    db_session.commit()
       
    return redirect(url_for('Regaderas'))

@app.get('/E_Regadera/<id>')
def E_Regadera(id):
   regadera = db_session.query(models.Regadera).get(id)
   
   if regadera == None:
       flash('ID no encontrado')
       return redirect(url_for('Regaderas'))
   
   image_paths = [regadera.Imagen, regadera.IMG2]
    
   base_path = 'static/imagenes/Griferia/Regaderas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(regadera)
   db_session.commit()
   
   return redirect(url_for('Regaderas'))  

#---------------- Brazos --------------
@app.post('/Add_Brazo')
def Add_Brazo():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Flu = request.form['Flujo_agua']
    Presion = request.form['Presion']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Brazo'], new_filename))
                return os.path.join(app.config['IMGS_GF_Brazo'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_brazo = models.Brazo(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Flujo_agua =Flu,
        Presion =Presion,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_brazo)
    db_session.commit()
    return redirect("Brazos")

@app.post('/Act_Brazo/<id>')
def Act_Brazo(id):
    brazo_act = db_session.query(models.Brazo).get(id)
       
    if brazo_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Brazos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Flu_act = request.form['Flujo_agua_act']
    Presi_act = request.form['Presion_act']

    if brazo_act == None:
        flash('No hay nada')
        return redirect (url_for('Brazos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Brazo'], new_filename))
                return os.path.join(app.config['IMGS_GF_Brazo'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    brazo_act.Imagen = update_image('Imagen_act', brazo_act.Imagen)
    brazo_act.IMG2 = update_image('IMG2_act', brazo_act.IMG2)
       
    brazo_act.Nombre = Name_act
    brazo_act.Precio = Prec_act
    brazo_act.Codigo = Cod_act
    brazo_act.Marca = Marc_act
    brazo_act.Color = Col_act
    brazo_act.Medida = Med_act
    brazo_act.Material = Mat_act
    brazo_act.Flujo_agua = Flu_act
    brazo_act.Presion = Presi_act
       
    db_session.add(brazo_act)
    db_session.commit()
       
    return redirect(url_for('Brazos'))

@app.get('/E_Brazo/<id>')
def E_Brazo(id):
   brazos = db_session.query(models.Brazo).get(id)
   
   if brazos == None:
       flash('ID no encontrado')
       return redirect(url_for('Brazos'))
   
   image_paths = [brazos.Imagen, brazos.IMG2]
    
   base_path = 'static/imagenes/Griferia/Brazos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(brazos)
   db_session.commit()
   
   return redirect(url_for('Brazos')) 

#---------------- Tocadores --------------
@app.post('/Add_Tocador')
def Add_Tocador():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Tocador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tocador'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_tocador = models.Tocador(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_tocador)
    db_session.commit()
    return redirect("Tocadores")

@app.post('/Act_Tocador/<id>')
def Act_Tocador(id):
    tocador_act = db_session.query(models.Tocador).get(id)
       
    if tocador_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tocadores'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']

    if tocador_act == None:
        flash('No hay nada')
        return redirect (url_for('Tocadores'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Tocador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tocador'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    tocador_act.Imagen = update_image('Imagen_act', tocador_act.Imagen)
    tocador_act.IMG2 = update_image('IMG2_act', tocador_act.IMG2)
       
    tocador_act.Nombre = Name_act
    tocador_act.Precio = Prec_act
    tocador_act.Codigo = Cod_act
    tocador_act.Marca = Marc_act
    tocador_act.Color = Col_act
    tocador_act.Medida = Med_act
    tocador_act.Material = Mat_act
       
    db_session.add(tocador_act)
    db_session.commit()
       
    return redirect(url_for('Tocadores'))

@app.get('/E_Tocador/<id>')
def E_Tocador(id):
   tocador = db_session.query(models.Tocador).get(id)
   
   if tocador == None:
       flash('ID no encontrado')
       return redirect(url_for('Tocadores'))
   
   image_paths = [tocador.Imagen, tocador.IMG2]
    
   base_path = 'static/imagenes/Griferia/Tocadores'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(tocador)
   db_session.commit()
   
   return redirect(url_for('Tocadores'))  

#---------------- Parrillas --------------
@app.post('/Add_Parrilla')
def Add_Parrilla():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Comp = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Parrilla'], new_filename))
                return os.path.join(app.config['IMGS_GF_Parrilla'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_parrilla = models.Parrilla(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Complementos =Comp,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_parrilla)
    db_session.commit()
    return redirect("Parrillas")

@app.post('/Act_Parrilla/<id>')
def Act_Parrilla(id):
    parrilla_act = db_session.query(models.Parrilla).get(id)
       
    if parrilla_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Parrillas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Comp_act = request.form['Complementos_act']
    
    if parrilla_act == None:
        flash('No hay nada')
        return redirect (url_for('Parrillas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Parrilla'], new_filename))
                return os.path.join(app.config['IMGS_GF_Parrilla'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    parrilla_act.Imagen = update_image('Imagen_act', parrilla_act.Imagen)
    parrilla_act.IMG2 = update_image('IMG2_act', parrilla_act.IMG2)
       
    parrilla_act.Nombre = Name_act
    parrilla_act.Precio = Prec_act
    parrilla_act.Codigo = Cod_act
    parrilla_act.Marca = Marc_act
    parrilla_act.Color = Col_act
    parrilla_act.Medida = Med_act
    parrilla_act.Material = Mat_act
    parrilla_act.Complementos = Comp_act
       
    db_session.add(parrilla_act)
    db_session.commit()
       
    return redirect(url_for('Parrillas'))

@app.get('/E_Parrilla/<id>')
def E_Parrilla(id):
   parrilla = db_session.query(models.Parrilla).get(id)
   
   if parrilla == None:
       flash('ID no encontrado')
       return redirect(url_for('Parrillas'))
   
   image_paths = [parrilla.Imagen, parrilla.IMG2]
    
   base_path = 'static/imagenes/Griferia/Parrillas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(parrilla)
   db_session.commit()
   
   return redirect(url_for('Parrillas'))  

#---------------- Campanas --------------
@app.post('/Add_Campana')
def Add_Campana():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Comp = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Campana'], new_filename))
                return os.path.join(app.config['IMGS_GF_Campana'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_campana = models.Campana(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Complementos =Comp,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_campana)
    db_session.commit()
    return redirect("Campanas")

@app.post('/Act_Campana/<id>')
def Act_Campana(id):
    campana_act = db_session.query(models.Campana).get(id)
       
    if campana_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Campanas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Comp_act = request.form['Complementos_act']
    
    if campana_act == None:
        flash('No hay nada')
        return redirect (url_for('Campanas'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Campana'], new_filename))
                return os.path.join(app.config['IMGS_GF_Campana'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    campana_act.Imagen = update_image('Imagen_act', campana_act.Imagen)
    campana_act.IMG2 = update_image('IMG2_act', campana_act.IMG2)
    
    campana_act.Nombre = Name_act
    campana_act.Precio = Prec_act
    campana_act.Codigo = Cod_act
    campana_act.Marca = Marc_act
    campana_act.Color = Col_act
    campana_act.Medida = Med_act
    campana_act.Material = Mat_act
    campana_act.Complementos = Comp_act
       
    db_session.add(campana_act)
    db_session.commit()
       
    return redirect(url_for('Campanas'))

@app.get('/E_Campana/<id>')
def E_Campana(id):
   campana = db_session.query(models.Campana).get(id)
   
   if campana == None:
       flash('ID no encontrado')
       return redirect(url_for('Campanas'))
   
   image_paths = [campana.Imagen, campana.IMG2]
    
   base_path = 'static/imagenes/Griferia/Campanas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(campana)
   db_session.commit()
   
   return redirect(url_for('Campanas')) 

#---------------- Tarjas --------------
@app.post('/Add_Tarja')
def Add_Tarja():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Tarja'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tarja'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_tarja = models.Tarja(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_tarja)
    db_session.commit()
    return redirect("Tarjas")

@app.post('/Act_Tarja/<id>')
def Act_Tarja(id):
    tarja_act = db_session.query(models.Tarja).get(id)
       
    if tarja_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tarjas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
       
    if tarja_act == None:
        flash('No hay nada')
        return redirect (url_for('Tarjas'))
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Tarja'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tarja'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    tarja_act.Imagen = update_image('Imagen_act', tarja_act.Imagen)
    tarja_act.IMG2 = update_image('IMG2_act', tarja_act.IMG2)
       
    tarja_act.Nombre = Name_act
    tarja_act.Precio = Prec_act
    tarja_act.Codigo = Cod_act
    tarja_act.Marca = Marc_act
    tarja_act.Color = Col_act
    tarja_act.Medida = Med_act
    tarja_act.Material = Mat_act
       
    db_session.add(tarja_act)
    db_session.commit()
       
    return redirect(url_for('Tarjas'))

@app.get('/E_Tarja/<id>')
def E_Tarja(id):
   tarja = db_session.query(models.Tarja).get(id)
   
   if tarja == None:
       flash('ID no encontrado')
       return redirect(url_for('Tarjas'))
   
   image_paths = [tarja.Imagen, tarja.IMG2]
    
   base_path = 'static/imagenes/Griferia/Tarjas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(tarja)
   db_session.commit()
   
   return redirect(url_for('Tarjas')) 

#---------------- Accesorios --------------
@app.post('/Add_Accesorio')
def Add_Accesorio():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Com = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Accesorio'], new_filename))
                return os.path.join(app.config['IMGS_GF_Accesorio'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_accesorio = models.Accesorio(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Complementos = Com,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_accesorio)
    db_session.commit()
    return redirect("Accesorios")

@app.post('/Act_Accesorio/<id>')
def Act_Accesorio(id):
    acceso_act = db_session.query(models.Accesorio).get(id)
       
    if acceso_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Accesorios'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Com_act = request.form['Complementos_act']
    
    if acceso_act == None:
        flash('No hay nada')
        return redirect (url_for('Accesorios'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Accesorio'], new_filename))
                return os.path.join(app.config['IMGS_GF_Accesorio'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    acceso_act.Imagen = update_image('Imagen_act', acceso_act.Imagen)
    acceso_act.IMG2 = update_image('IMG2_act', acceso_act.IMG2)
       
    acceso_act.Nombre = Name_act
    acceso_act.Precio = Prec_act
    acceso_act.Codigo = Cod_act
    acceso_act.Marca = Marc_act
    acceso_act.Color = Col_act
    acceso_act.Material = Mat_act
    acceso_act.Complementos = Com_act

    db_session.add(acceso_act)
    db_session.commit()
       
    return redirect(url_for('Accesorios'))

@app.get('/E_Accesorio/<id>')
def E_Accesorio(id):
   acceso = db_session.query(models.Accesorio).get(id)
   
   if acceso == None:
       flash('ID no encontrado')
       return redirect(url_for('Accesorios'))
   
   image_paths = [acceso.Imagen, acceso.IMG2]
    
   base_path = 'static/imagenes/Griferia/Accesorios'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(acceso)
   db_session.commit()
   
   return redirect(url_for('Accesorios')) 

#---------------- Dispensadores --------------
@app.post('/Add_Dispensador')
def Add_Dispensador():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cap = request.form['Capacidad']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Dispensador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Dispensador'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_dispensador = models.Dispensador(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Capacidad = Cap,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_dispensador)
    db_session.commit()
    return redirect("Dispensadores")

@app.post('/Act_Dispensador/<id>')
def Act_Dispensador(id):
    dispen_act = db_session.query(models.Dispensador).get(id)
       
    if dispen_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Dispensadores'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Cap_act = request.form['Capacidad_act']

    if dispen_act == None:
        flash('No hay nada')
        return redirect (url_for('Dispensadores'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Dispensador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Dispensador'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    dispen_act.Imagen = update_image('Imagen_act', dispen_act.Imagen)
    dispen_act.IMG2 = update_image('IMG2_act', dispen_act.IMG2)
       
    dispen_act.Nombre = Name_act
    dispen_act.Precio = Prec_act
    dispen_act.Codigo = Cod_act
    dispen_act.Marca = Marc_act
    dispen_act.Color = Col_act
    dispen_act.Material = Mat_act
    dispen_act.Capacidad = Cap_act
       
    db_session.add(dispen_act)
    db_session.commit()
       
    return redirect(url_for('Dispensadores'))

@app.get('/E_Dispensador/<id>')
def E_Dispensador(id):
   dispe = db_session.query(models.Dispensador).get(id)
   
   if dispe == None:
       flash('ID no encontrado')
       return redirect(url_for('Dispensadores'))
   
   image_paths = [dispe.Imagen, dispe.IMG2]
    
   base_path = 'static/imagenes/Griferia/Dispensadores'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(dispe)
   db_session.commit()
   
   return redirect(url_for('Dispensadores')) 

#---------------- Mezcladoras --------------
@app.post('/Add_Mezcladora')
def Add_Mezcladora():
    Name = request.form['Nombre']
    PreC = request.form['Precio']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Pre = request.form['Presion']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Mezcladora'], new_filename))
                return os.path.join(app.config['IMGS_GF_Mezcladora'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_mezcla = models.Mezcladora(
        Nombre = Name,
        Precio = PreC,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Presion = Pre,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_mezcla)
    db_session.commit()
    return redirect("Mezcladoras")

@app.post('/Act_Mezcladora/<id>')
def Act_Mezcladora(id):
    mezcla_act = db_session.query(models.Mezcladora).get(id)
       
    if mezcla_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Mezcladoras'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Pre_act = request.form['Presion_act']
    
    if mezcla_act == None:
        flash('No hay nada')
        return redirect (url_for('Mezcladoras'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Mezcladora'], new_filename))
                return os.path.join(app.config['IMGS_GF_Mezcladora'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    mezcla_act.Imagen = update_image('Imagen_act', mezcla_act.Imagen)
    mezcla_act.IMG2 = update_image('IMG2_act', mezcla_act.IMG2)
       
    mezcla_act.Nombre = Name_act
    mezcla_act.Precio = Prec_act
    mezcla_act.Codigo = Cod_act
    mezcla_act.Marca = Marc_act
    mezcla_act.Color = Col_act
    mezcla_act.Material = Mat_act
    mezcla_act.Presion = Pre_act

    db_session.add(mezcla_act)
    db_session.commit()
       
    return redirect(url_for('Mezcladoras'))

@app.get('/E_Mezcladora/<id>')
def E_Mezcladora(id):
   mezcla = db_session.query(models.Mezcladora).get(id)
   
   if mezcla == None:
       flash('ID no encontrado')
       return redirect(url_for('Mezcladoras'))
   
   image_paths = [mezcla.Imagen, mezcla.IMG2]
    
   base_path = 'static/imagenes/Griferia/Mezcladoras'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(mezcla)
   db_session.commit()
   
   return redirect(url_for('Mezcladoras')) 

#---------------- Monomandos --------------
@app.post('/Add_Monomando')
def Add_Monomando():
    Name = request.form['Nombre']
    Prec = request.form['Precio']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Pre = request.form['Presion']
    Comp = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Monomando'], new_filename))
                return os.path.join(app.config['IMGS_GF_Monomando'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_mono = models.Monomando(
        Nombre = Name,
        Precio = Prec,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Presion = Pre,
        Complementos = Comp,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_mono)
    db_session.commit()
    return redirect("Monomandos")

@app.post('/Act_Monomando/<id>')
def Act_Monomando(id):
    mono_act = db_session.query(models.Monomando).get(id)
       
    if mono_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Monomandos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Pre_act = request.form['Presion_act']
    Comp_act = request.form['Complementos_act']
       
    if mono_act == None:
        flash('No hay nada')
        return redirect (url_for('Monomandos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Monomando'], new_filename))
                return os.path.join(app.config['IMGS_GF_Monomando'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    mono_act.Imagen = update_image('Imagen_act', mono_act.Imagen)
    mono_act.IMG2 = update_image('IMG2_act', mono_act.IMG2)
       
    mono_act.Nombre = Name_act
    mono_act.Precio = Prec_act
    mono_act.Codigo = Cod_act
    mono_act.Marca = Marc_act
    mono_act.Color = Col_act
    mono_act.Material = Mat_act
    mono_act.Presion = Pre_act
    mono_act.Complementos = Comp_act

    db_session.add(mono_act)
    db_session.commit()
       
    return redirect(url_for('Monomandos'))

@app.get('/E_Monomando/<id>')
def E_Monomando(id):
   mono = db_session.query(models.Monomando).get(id)
   
   if mono == None:
       flash('ID no encontrado')
       return redirect(url_for('Monomandos'))
   
   image_paths = [mono.Imagen, mono.IMG2]
    
   base_path = 'static/imagenes/Griferia/Monomandos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(mono)
   db_session.commit()
   
   return redirect(url_for('Monomandos')) 

#---------------- Kits de instalación --------------
@app.post('/Add_Kit')
def Add_Kit():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med_ll = request.form['Medida_llaves']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Contra = request.form['Contracanasta']
    Ali = request.form['Alimentador']
    Comp = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_KitInstall'], new_filename))
                return os.path.join(app.config['IMGS_GF_KitInstall'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_kit = models.Kits_install(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida_llaves = Med_ll,
        Marca =Marc,
        Material =Mat,
        Contracanasta = Contra,
        Alimentador = Ali,
        Complementos = Comp,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_kit)
    db_session.commit()
    return redirect("Kits")

@app.post('/Act_Kit/<id>')
def Act_Kit(id):
    kit_act = db_session.query(models.Kits_install).get(id)
       
    if kit_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Kits'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Med_ll_act = request.form['Medida_llaves_act']
    Mat_act = request.form['Material_act']
    Contra_act = request.form['Contracanasta_act']
    Ali_act = request.form['Alimentador_act']
    Comp_act = request.form['Complementos_act']

    if kit_act == None:
        flash('No hay nada')
        return redirect (url_for('Kits'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_KitInstall'], new_filename))
                return os.path.join(app.config['IMGS_GF_KitInstall'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    kit_act.Imagen = update_image('Imagen_act', kit_act.Imagen)
    kit_act.IMG2 = update_image('IMG2_act', kit_act.IMG2)
       
    kit_act.Nombre = Name_act
    kit_act.Precio = Prec_act
    kit_act.Codigo = Cod_act
    kit_act.Marca = Marc_act
    kit_act.Medida_llaves = Med_ll_act
    kit_act.Material = Mat_act
    kit_act.Contracanasta = Contra_act
    kit_act.Alimentador = Ali_act
    kit_act.Complementos = Comp_act

    db_session.add(kit_act)
    db_session.commit()
       
    return redirect(url_for('Kits'))

@app.get('/E_Kit/<id>')
def E_Kit(id):
   kit = db_session.query(models.Kits_install).get(id)
   
   if kit == None:
       flash('ID no encontrado')
       return redirect(url_for('Kits'))
   
   image_paths = [kit.Imagen, kit.IMG2]
    
   base_path = 'static/imagenes/Griferia/KitsInstalls'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(kit)
   db_session.commit()
   
   return redirect(url_for('Kits')) 

#---------------- Persianas --------------
@app.post('/Add_Persiana')
def Add_Persiana():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Comp = request.form['Complementos']
    Tiem = request.form['Tiempo_entrega']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Persiana'], new_filename))
                return os.path.join(app.config['IMGS_GF_Persiana'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_persiana = models.Persiana(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Tiempo_entrega = Tiem,
        Complementos = Comp,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_persiana)
    db_session.commit()
    return redirect("Persianas")

@app.post('/Act_Persiana/<id>')
def Act_Persiana(id):
    persi_act = db_session.query(models.Persiana).get(id)
       
    if persi_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Persianas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Comp_act = request.form['Complementos_act']
    Tiem_act = request.form['Tiempo_entrega_act']

    if persi_act == None:
        flash('No hay nada')
        return redirect (url_for('Persianas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Persiana'], new_filename))
                return os.path.join(app.config['IMGS_GF_Persiana'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    persi_act.Imagen = update_image('Imagen_act', persi_act.Imagen)
    persi_act.IMG2 = update_image('IMG2_act', persi_act.IMG2)
       
    persi_act.Nombre = Name_act
    persi_act.Precio = Prec_act
    persi_act.Codigo = Cod_act
    persi_act.Marca = Marc_act
    persi_act.Color = Col_act
    persi_act.Material = Mat_act
    persi_act.Complementos = Comp_act
    persi_act.Tiempo_entrega = Tiem_act
       
    db_session.add(persi_act)
    db_session.commit()
       
    return redirect(url_for('Persianas'))

@app.get('/E_Persiana/<id>')
def E_Persiana(id):
   persi = db_session.query(models.Persiana).get(id)
   
   if persi == None:
       flash('ID no encontrado')
       return redirect(url_for('Persianas'))
   
   image_paths = [persi.Imagen, persi.IMG2]
    
   base_path = 'static/imagenes/Griferia/Persianas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(persi)
   db_session.commit()
   
   return redirect(url_for('Persianas')) 

#---------------- Tapetes --------------
@app.post('/Add_Tapete')
def Add_Tapete():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Tapete'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tapete'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_tapete = models.Tapete(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_tapete)
    db_session.commit()
    return redirect("Tapetes")

@app.post('/Act_Tapete/<id>')
def Act_Tapete(id):
    tapete_act = db_session.query(models.Tapete).get(id)
       
    if tapete_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tapetes'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']

    if tapete_act == None:
        flash('No hay nada')
        return redirect (url_for('Tapetes'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Tapete'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tapete'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    tapete_act.Imagen = update_image('Imagen_act', tapete_act.Imagen)
    tapete_act.IMG2 = update_image('IMG2_act', tapete_act.IMG2)
       
    tapete_act.Nombre = Name_act
    tapete_act.Precio = Prec_act
    tapete_act.Codigo = Cod_act
    tapete_act.Marca = Marc_act
    tapete_act.Color = Col_act
    tapete_act.Medida = Med_act
    tapete_act.Material = Mat_act
    
    db_session.add(tapete_act)
    db_session.commit()
       
    return redirect(url_for('Tapetes'))

@app.get('/E_Tapete/<id>')
def E_Tapete(id):
   tapete = db_session.query(models.Tapete).get(id)
   
   if tapete == None:
       flash('ID no encontrado')
       return redirect(url_for('Tapetes'))
   
   image_paths = [tapete.Imagen, tapete.IMG2]
    
   base_path = 'static/imagenes/Griferia/Tapetes'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(tapete)
   db_session.commit()
   
   return redirect(url_for('Tapetes'))  

#---------------- Organizadores --------------
@app.post('/Add_hola')
def Add_Organizador():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Organizador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Organizador'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_orga = models.Organizador(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_orga)
    db_session.commit()
    return redirect("Organizadores")

@app.post('/Act_Organizador/<id>')
def Act_Organizador(id):
    orga_act = db_session.query(models.Organizador).get(id)
    if orga_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Organizadores'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
       
    if orga_act == None:
        flash('No hay nada')
        return redirect (url_for('Organizadores'))
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Organizador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Organizador'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    orga_act.Imagen = update_image('Imagen_act', orga_act.Imagen)
    orga_act.IMG2 = update_image('IMG2_act', orga_act.IMG2)
       
    orga_act.Nombre = Name_act
    orga_act.Precio = Prec_act
    orga_act.Codigo = Cod_act
    orga_act.Marca = Marc_act
    orga_act.Color = Col_act
    orga_act.Medida = Med_act
    orga_act.Material = Mat_act

    db_session.add(orga_act)
    db_session.commit()
       
    return redirect(url_for('Organizadores'))

@app.get('/E_Organizador/<id>')
def E_Organizador(id):
   orga = db_session.query(models.Organizador).get(id)
   
   if orga == None:
       flash('ID no encontrado')
       return redirect(url_for('Organizadores'))
   
   image_paths = [orga.Imagen, orga.IMG2]
    
   base_path = 'static/imagenes/Griferia/Organizadores'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(orga)
   db_session.commit()
   
   return redirect(url_for('Organizadores'))  

#---------------- Asientos --------------
@app.post('/Add_Asiento')
def Add_Asiento():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Tip = request.form['Tipo']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Asiento'], new_filename))
                return os.path.join(app.config['IMGS_GF_Asiento'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_asiento = models.Asiento(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Tipo =Tip,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_asiento)
    db_session.commit()
    return redirect("Asientos")

@app.post('/Act_Asiento/<id>')
def Act_Asiento(id):
    asiento_act = db_session.query(models.Asiento).get(id)
       
    if asiento_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Asientos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Tip_act = request.form['Tipo_act']
    
    if asiento_act == None:
        flash('No hay nada')
        return redirect (url_for('Asientos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Asiento'], new_filename))
                return os.path.join(app.config['IMGS_GF_Asiento'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    asiento_act.Imagen = update_image('Imagen_act', asiento_act.Imagen)
    asiento_act.IMG2 = update_image('IMG2_act', asiento_act.IMG2)
       
    asiento_act.Nombre = Name_act
    asiento_act.Precio = Prec_act
    asiento_act.Codigo = Cod_act
    asiento_act.Marca = Marc_act
    asiento_act.Color = Col_act
    asiento_act.Medida = Med_act
    asiento_act.Tipo = Tip_act

    db_session.add(asiento_act)
    db_session.commit()
       
    return redirect(url_for('Asientos'))

@app.get('/E_Asiento/<id>')
def E_Asiento(id):
   asiento = db_session.query(models.Asiento).get(id)
   
   if asiento == None:
       flash('ID no encontrado')
       return redirect(url_for('Asientos'))
   
   image_paths = [asiento.Imagen, asiento.IMG2]
    
   base_path = 'static/imagenes/Griferia/Asientos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(asiento)
   db_session.commit()
   
   return redirect(url_for('Asientos'))  

#---------------- Ovalines --------------
@app.post('/Add_Ovalin')
def Add_Ovalin():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Tip = request.form['Tipo_colocacion']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Ovalin'], new_filename))
                return os.path.join(app.config['IMGS_GF_Ovalin'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_ovalin = models.Ovalin(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Tipo_colocacion =Tip,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_ovalin)
    db_session.commit()
    return redirect("Ovalines")

@app.post('/Act_Ovalin/<id>')
def Act_Ovalin(id):
    ovalin_act = db_session.query(models.Ovalin).get(id)
       
    if ovalin_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Ovalines'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Tip_act = request.form['Tipo_colocacion_act']
    
    if ovalin_act == None:
        flash('No hay nada')
        return redirect (url_for('Ovalines'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Ovalin'], new_filename))
                return os.path.join(app.config['IMGS_GF_Ovalin'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    ovalin_act.Imagen = update_image('Imagen_act', ovalin_act.Imagen)
    ovalin_act.IMG2 = update_image('IMG2_act', ovalin_act.IMG2)
       
    ovalin_act.Nombre = Name_act
    ovalin_act.Precio = Prec_act
    ovalin_act.Codigo = Cod_act
    ovalin_act.Marca = Marc_act
    ovalin_act.Color = Col_act
    ovalin_act.Medida = Med_act
    ovalin_act.Material = Mat_act
    ovalin_act.Tipo_colocacion = Tip_act

    db_session.add(ovalin_act)
    db_session.commit()
       
    return redirect(url_for('Ovalines'))

@app.get('/E_Ovalin/<id>')
def E_Ovalin(id):
   ovalin = db_session.query(models.Ovalin).get(id)
   if ovalin == None:
       flash('ID no encontrado')
       return redirect(url_for('Ovalines'))
   
   image_paths = [ovalin.Imagen, ovalin.IMG2]
    
   base_path = 'static/imagenes/Griferia/Ovalines'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(ovalin)
   db_session.commit()
   return redirect(url_for('Ovalines'))  

#---------------- Separadores --------------
@app.post('/Add_Separador')
def Add_Separador():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Separador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Separador'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_separador = models.Separador(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_separador)
    db_session.commit()
    return redirect("Separadores")

@app.post('/Act_Separador/<id>')
def Act_Separador(id):
    separador_act = db_session.query(models.Separador).get(id)
       
    if separador_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Separadores'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
      
    if separador_act == None:
        flash('No hay nada')
        return redirect (url_for('Separadores'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Separador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Separador'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    separador_act.Imagen = update_image('Imagen_act', separador_act.Imagen)
    separador_act.IMG2 = update_image('IMG2_act', separador_act.IMG2)
       
    separador_act.Nombre = Name_act
    separador_act.Precio = Prec_act
    separador_act.Codigo = Cod_act
    separador_act.Marca = Marc_act
    separador_act.Color = Col_act
    separador_act.Medida = Med_act
    separador_act.Material = Mat_act

    db_session.add(separador_act)
    db_session.commit()
       
    return redirect(url_for('Separadores'))

@app.get('/E_Separador/<id>')
def E_Separador(id):
   sepa = db_session.query(models.Separador).get(id)
   
   if sepa == None:
       flash('ID no encontrado')
       return redirect(url_for('Separadores'))
   
   image_paths = [sepa.Imagen, sepa.IMG2]
    
   base_path = 'static/imagenes/Griferia/Separadores'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(sepa)
   db_session.commit()
   
   return redirect(url_for('Separadores')) 

#---------------- Herramientas --------------
@app.post('/Add_Herramienta')
def Add_Herramienta():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_HerramientaCol'], new_filename))
                return os.path.join(app.config['IMGS_GF_HerramientaCol'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_herra = models.Herramienta_Col(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_herra)
    db_session.commit()
    return redirect("Herramientas")

@app.post('/Act_Herramienta/<id>')
def Act_Herramienta(id):
    herra_act = db_session.query(models.Herramienta_Col).get(id)
       
    if herra_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Herramientas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']

    if herra_act == None:
        flash('No hay nada')
        return redirect (url_for('Herramientas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_HerramientaCol'], new_filename))
                return os.path.join(app.config['IMGS_GF_HerramientaCol'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    herra_act.Imagen = update_image('Imagen_act', herra_act.Imagen)
    herra_act.IMG2 = update_image('IMG2_act', herra_act.IMG2)
       
    herra_act.Nombre = Name_act
    herra_act.Precio = Prec_act
    herra_act.Codigo = Cod_act
    herra_act.Marca = Marc_act
    herra_act.Medida = Med_act
    herra_act.Material = Mat_act

    db_session.add(herra_act)
    db_session.commit()
       
    return redirect(url_for('Herramientas'))

@app.get('/E_Herramienta/<id>')
def E_Herramienta(id):
   herr = db_session.query(models.Herramienta_Col).get(id)
   
   if herr == None:
       flash('ID no encontrado')
       return redirect(url_for('Herramientas'))
   
   image_paths = [herr.Imagen, herr.IMG2]
    
   base_path = 'static/imagenes/Griferia/Herramientas_Col'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(herr)
   db_session.commit()
   
   return redirect(url_for('Herramientas'))  

#---------------- Calentadores Solares --------------
@app.post('/Add_CalentadorS')
def Add_CalentadorS():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cap = request.form['Capacidad']
    Com = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_CalentadorS'], new_filename))
                return os.path.join(app.config['IMGS_GF_CalentadorS'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_calentador = models.Calentador_S(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        color = Col,
        Marca =Marc,
        Material =Mat,
        Capacidad = Cap,
        Complementos = Com,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_calentador)
    db_session.commit()
    return redirect("CalentadoresS")

@app.post('/Act_CalentadorS/<id>')
def Act_CalentadorS(id):
    calentador_act = db_session.query(models.Calentador_S).get(id)
       
    if calentador_act == None:
        flash('ID no encontrado')
        return redirect (url_for('CalentadoresS'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Col_act = request.form['Color_act']
    Marc_act = request.form['Marca_act']
    Mat_act = request.form['Material_act']
    Cap_act = request.form['Capacidad_act']
    Com_act = request.form['Complementos_act']
      
    if calentador_act == None:
        flash('No hay nada')
        return redirect (url_for('CalentadoresS'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_CalentadorS'], new_filename))
                return os.path.join(app.config['IMGS_GF_CalentadorS'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    calentador_act.Imagen = update_image('Imagen_act', calentador_act.Imagen)
    calentador_act.IMG2 = update_image('IMG2_act', calentador_act.IMG2)
       
    calentador_act.Nombre = Name_act
    calentador_act.Precio = Prec_act
    calentador_act.Codigo = Cod_act
    calentador_act.color = Col_act
    calentador_act.Marca = Marc_act
    calentador_act.Material = Mat_act
    calentador_act.Capacidad = Cap_act
    calentador_act.Complementos = Com_act

    db_session.add(calentador_act)
    db_session.commit()
       
    return redirect(url_for('CalentadoresS'))

@app.get('/E_CalentadorS/<id>')
def E_CalentadorS(id):
   CalentadorS = db_session.query(models.Calentador_S).get(id)
   
   if CalentadorS == None:
       flash('ID no encontrado')
       return redirect(url_for('CalentadoresS'))
   
   image_paths = [CalentadorS.Imagen, CalentadorS.IMG2]
    
   base_path = 'static/imagenes/Griferia/Calentadores_S'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(CalentadorS)
   db_session.commit()
   
   return redirect(url_for('CalentadoresS'))  

#---------------- Calentadores de Paso --------------
@app.post('/Add_CalentadorP')
def Add_CalentadorP():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cap = request.form['Capacidad']
    Serv = request.form['Servicio']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_CalentadorP'], new_filename))
                return os.path.join(app.config['IMGS_GF_CalentadorP'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_calentadorp = models.Calentador_P(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        color = Col,
        Marca =Marc,
        Material =Mat,
        Capacidad = Cap,
        Servicios = Serv,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_calentadorp)
    db_session.commit()
    return redirect("CalentadoresP")

@app.post('/Act_CalentadorP/<id>')
def Act_CalentadorP(id):
    calentadorp_act = db_session.query(models.Calentador_P).get(id)
       
    if calentadorp_act == None:
        flash('ID no encontrado')
        return redirect (url_for('CalentadoresP'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Col_act = request.form['Color_act']
    Marc_act = request.form['Marca_act']
    Mat_act = request.form['Material_act']
    Cap_act = request.form['Capacidad_act']
    Serv_act = request.form['Servicio_act']
       
    if calentadorp_act == None:
        flash('No hay nada')
        return redirect (url_for('CalentadoresP'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_CalentadorP'], new_filename))
                return os.path.join(app.config['IMGS_GF_CalentadorP'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    calentadorp_act.Imagen = update_image('Imagen_act', calentadorp_act.Imagen)
    calentadorp_act.IMG2 = update_image('IMG2_act', calentadorp_act.IMG2)
       
    calentadorp_act.Nombre = Name_act
    calentadorp_act.Precio = Prec_act
    calentadorp_act.Codigo = Cod_act
    calentadorp_act.color = Col_act
    calentadorp_act.Marca = Marc_act
    calentadorp_act.Material = Mat_act
    calentadorp_act.Capacidad = Cap_act
    calentadorp_act.Servicios = Serv_act
   
    db_session.add(calentadorp_act)
    db_session.commit()
       
    return redirect(url_for('CalentadoresP'))

@app.get('/E_CalentadorP/<id>')
def E_CalentadorP(id):
   CalentadorP = db_session.query(models.Calentador_P).get(id)
   
   if CalentadorP == None:
       flash('ID no encontrado')
       return redirect(url_for('CalentadoresP'))
   
   image_paths = [CalentadorP.Imagen, CalentadorP.IMG2]
    
   base_path = 'static/imagenes/Griferia/Calentadores_P'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(CalentadorP)
   db_session.commit()
   
   return redirect(url_for('CalentadoresP'))

#---------------- Espejos --------------
@app.post('/Add_Espejo')
def Add_Espejo():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Mat = request.form['Material']
    Com = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Espejo'], new_filename))
                return os.path.join(app.config['IMGS_GF_Espejo'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_espejo = models.Espejo(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        color = Col,
        Complementos =Com,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_espejo)
    db_session.commit()
    return redirect("Espejos")

@app.post('/Act_Espejo/<id>')
def Act_Espejo(id):
    espejo_act = db_session.query(models.Espejo).get(id)
       
    if espejo_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Espejos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Med_act = request.form['Medida_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Com_act = request.form['Complementos_act']  
       
    if espejo_act == None:
        flash('No hay nada')
        return redirect (url_for('Espejos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Espejo'], new_filename))
                return os.path.join(app.config['IMGS_GF_Espejo'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    espejo_act.Imagen = update_image('Imagen_act', espejo_act.Imagen)
    espejo_act.IMG2 = update_image('IMG2_act', espejo_act.IMG2)
       
    espejo_act.Nombre = Name_act
    espejo_act.Precio = Prec_act
    espejo_act.Codigo = Cod_act
    espejo_act.Medida = Med_act
    espejo_act.color = Col_act
    espejo_act.Material = Mat_act
    espejo_act.Complementos = Com_act

    db_session.add(espejo_act)
    db_session.commit()
       
    return redirect(url_for('Espejos'))

@app.get('/E_Espejo/<id>')
def E_Espejo(id):
   espejo = db_session.query(models.Espejo).get(id)
   
   if espejo == None:
       flash('ID no encontrado')
       return redirect(url_for('Espejos'))
   
   image_paths = [espejo.Imagen, espejo.IMG2]
    
   base_path = 'static/imagenes/Griferia/Espejos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(espejo)
   db_session.commit()
   
   return redirect(url_for('Espejos')) 

#---------------- Repisas --------------
@app.post('/Add_Repisa')
def Add_Repisa():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Repisa'], new_filename))
                return os.path.join(app.config['IMGS_GF_Repisa'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_repisa = models.Repisa(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca = Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_repisa)
    db_session.commit()
    return redirect("Repisas")

@app.post('/Act_Repisa/<id>')
def Act_Repisa(id):
    repisa_act = db_session.query(models.Repisa).get(id)
       
    if repisa_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Repisas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Med_act = request.form['Medida_act']
    Col_act = request.form['Color_act']
    Marc_act = request.form['Marca_act']
    Mat_act = request.form['Material_act']
       
    if repisa_act == None:
        flash('No hay nada')
        return redirect (url_for('Repisas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Repisa'], new_filename))
                return os.path.join(app.config['IMGS_GF_Repisa'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    repisa_act.Imagen = update_image('Imagen_act', repisa_act.Imagen)
    repisa_act.IMG2 = update_image('IMG2_act', repisa_act.IMG2)
       
    repisa_act.Nombre = Name_act
    repisa_act.Precio = Prec_act
    repisa_act.Codigo = Cod_act
    repisa_act.Medida = Med_act
    repisa_act.Color = Col_act
    repisa_act.Marca = Marc_act
    repisa_act.Material = Mat_act
 
    db_session.add(repisa_act)
    db_session.commit()
       
    return redirect(url_for('Repisas'))

@app.get('/E_Repisa/<id>')
def E_Repisa(id):
   repisa = db_session.query(models.Repisa).get(id)
   
   if repisa == None:
       flash('ID no encontrado')
       return redirect(url_for('Repisas'))
   
   image_paths = [repisa.Imagen, repisa.IMG2]
    
   base_path = 'static/imagenes/Griferia/Repisas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(repisa)
   db_session.commit()
   
   return redirect(url_for('Repisas')) 

#---------------- Resumideros --------------
@app.post('/Add_Resumidero')
def Add_Resumidero():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Resumidero'], new_filename))
                return os.path.join(app.config['IMGS_GF_Resumidero'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_resumidero = models.Resumidero(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_resumidero)
    db_session.commit()
    return redirect("Resumideros")

@app.post('/Act_Resumidero/<id>')
def Act_Resumidero(id):
    resu_act = db_session.query(models.Resumidero).get(id)
       
    if resu_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Resumideros'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Med_act = request.form['Medida_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']   
       
    if resu_act == None:
        flash('No hay nada')
        return redirect (url_for('Resumideros'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Resumidero'], new_filename))
                return os.path.join(app.config['IMGS_GF_Resumidero'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    resu_act.Imagen = update_image('Imagen_act', resu_act.Imagen)
    resu_act.IMG2 = update_image('IMG2_act', resu_act.IMG2)
       
    resu_act.Nombre = Name_act
    resu_act.Precio = Prec_act
    resu_act.Codigo = Cod_act
    resu_act.Medida = Med_act
    resu_act.Color = Col_act
    resu_act.Material = Mat_act

    db_session.add(resu_act)
    db_session.commit()
       
    return redirect(url_for('Resumideros'))

@app.get('/E_Resumidero/<id>')
def E_Resumidero(id):
   resumi = db_session.query(models.Resumidero).get(id)
   
   if resumi == None:
       flash('ID no encontrado')
       return redirect(url_for('Resumideros'))
   
   image_paths = [resumi.Imagen, resumi.IMG2]
    
   base_path = 'static/imagenes/Griferia/Resumideros'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(resumi)
   db_session.commit()
   
   return redirect(url_for('Resumideros')) 

#---------------- Cuadros --------------
@app.post('/Add_Cuadro')
def Add_Cuadro():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Cuadro'], new_filename))
                return os.path.join(app.config['IMGS_GF_Cuadro'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_cuadro = models.Cuadro(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_cuadro)
    db_session.commit()
    return redirect("Cuadros")

@app.post('/Act_Cuadro/<id>')
def Act_Cuadro(id):
    cuadro_act = db_session.query(models.Cuadro).get(id)
       
    if cuadro_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cuadros'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act'] 
       
    if cuadro_act == None:
        flash('No hay nada')
        return redirect (url_for('Cuadros'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Cuadro'], new_filename))
                return os.path.join(app.config['IMGS_GF_Cuadro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    cuadro_act.Imagen = update_image('Imagen_act', cuadro_act.Imagen)
    cuadro_act.IMG2 = update_image('IMG2_act', cuadro_act.IMG2)
       
    cuadro_act.Nombre = Name_act
    cuadro_act.Precio = Prec_act
    cuadro_act.Codigo = Cod_act
    cuadro_act.Medida = Med_act
    cuadro_act.Material = Mat_act
  
    db_session.add(cuadro_act)
    db_session.commit()
       
    return redirect(url_for('Cuadros'))

@app.get('/E_Cuadro/<id>')
def E_Cuadro(id):
   cuadro = db_session.query(models.Cuadro).get(id)
   
   if cuadro == None:
       flash('ID no encontrado')
       return redirect(url_for('Cuadros'))
   
   image_paths = [cuadro.Imagen, cuadro.IMG2]
    
   base_path = 'static/imagenes/Griferia/Cuadros'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(cuadro)
   db_session.commit()
   
   return redirect(url_for('Cuadros')) 

#---------------- Contra canastas --------------
@app.post('/Add_Contracanasta')
def Add_Contracanasta():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_ContraC'], new_filename))
                return os.path.join(app.config['IMGS_GF_ContraC'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_contraC = models.Contra_Can(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_contraC)
    db_session.commit()
    return redirect("Contracanastas")

@app.post('/Act_Contracanasta/<id>')
def Act_Contracanasta(id):
    contra_act = db_session.query(models.Contra_Can).get(id)
       
    if contra_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Contracanastas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
     
    if contra_act == None:
        flash('No hay nada')
        return redirect (url_for('Contracanastas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_ContraC'], new_filename))
                return os.path.join(app.config['IMGS_GF_ContraC'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    contra_act.Imagen = update_image('Imagen_act',contra_act.Imagen)
    contra_act.IMG2 = update_image('IMG2_act',contra_act.IMG2)
       
    contra_act.Nombre = Name_act
    contra_act.Precio = Prec_act
    contra_act.Codigo = Cod_act
    contra_act.Marca = Marc_act
    contra_act.Color = Col_act
    contra_act.Medida = Med_act
    contra_act.Material = Mat_act

    db_session.add(contra_act)
    db_session.commit()
       
    return redirect(url_for('Contracanastas'))

@app.get('/E_Contracanasta/<id>')
def E_Contracanasta(id):
   contra = db_session.query(models.Contra_Can).get(id)
   
   if contra == None:
       flash('ID no encontrado')
       return redirect(url_for('Contracanastas'))
   
   image_paths = [contra.Imagen, contra.IMG2]
    
   base_path = 'static/imagenes/Griferia/Contracanastas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(contra)
   db_session.commit()
   
   return redirect(url_for('Contracanastas')) 

#---------------- Cespol --------------
@app.post('/Add_Cespol')
def Add_Cespol():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Cespol'], new_filename))
                return os.path.join(app.config['IMGS_GF_Cespol'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_cespol = models.Cespol(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_cespol)
    db_session.commit()
    return redirect("Cespols")

@app.post('/Act_Cespol/<id>')
def Act_Cespol(id):
    cespol_act = db_session.query(models.Cespol).get(id)
       
    if cespol_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cespols'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    
    if cespol_act == None:
        flash('No hay nada')
        return redirect (url_for('Cespols'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Cespol'], new_filename))
                return os.path.join(app.config['IMGS_GF_Cespol'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    cespol_act.Imagen = update_image('Imagen_act', cespol_act.Imagen)
    cespol_act.IMG2 = update_image('IMG2_act', cespol_act.IMG2)
       
    cespol_act.Nombre = Name_act
    cespol_act.Precio = Prec_act
    cespol_act.Codigo = Cod_act
    cespol_act.Marca = Marc_act
    cespol_act.Color = Col_act
    cespol_act.Medida = Med_act
    cespol_act.Material = Mat_act

    db_session.add(cespol_act)
    db_session.commit()
       
    return redirect(url_for('Cespols'))

@app.get('/E_Cespol/<id>')
def E_Cespol(id):
   cespol = db_session.query(models.Cespol).get(id)
   
   if cespol == None:
       flash('ID no encontrado')
       return redirect(url_for('Cespols'))
   
   image_paths = [cespol.Imagen, cespol.IMG2]
    
   base_path = 'static/imagenes/Griferia/Cespols'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(cespol)
   db_session.commit()
   
   return redirect(url_for('Cespols')) 

#---------------- Impermeabilizantes --------------
@app.post('/Add_Imper')
def Add_Imper():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Cont = request.form['Contenido']
    Dur = request.form['Duracion']
    Car = request.form['Caracteristicas']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Impermeabilizante'], new_filename))
                return os.path.join(app.config['IMGS_GF_Impermeabilizante'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_imper = models.Impermeabilizante(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Color = Col,
        Marca =Marc,
        Contenido =Cont,
        Duracion = Dur,
        Caracteristicas = Car,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_imper)
    db_session.commit()
    return redirect("Impers")

@app.post('/Act_Imper/<id>')
def Act_Imper(id):
    imper_act = db_session.query(models.Impermeabilizante).get(id)
       
    if imper_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Impers'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Cont_act = request.form['Contenido_act']
    Dur_act = request.form['Duracion_act']
    Car_act = request.form['Caracteristicas_act']
 
    if imper_act == None:
        flash('No hay nada')
        return redirect (url_for('Impers'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Impermeabilizante'], new_filename))
                return os.path.join(app.config['IMGS_GF_Impermeabilizante'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    imper_act.Imagen = update_image('Imagen_act', imper_act.Imagen)
    imper_act.IMG2 = update_image('IMG2_act', imper_act.IMG2)
       
    imper_act.Nombre = Name_act
    imper_act.Precio = Prec_act
    imper_act.Codigo = Cod_act
    imper_act.Marca = Marc_act
    imper_act.Color = Col_act
    imper_act.Contenido = Cont_act
    imper_act.Duracion = Dur_act
    imper_act.Caracteristicas = Car_act

    db_session.add(imper_act)
    db_session.commit()
       
    return redirect(url_for('Impers'))

@app.get('/E_Imper/<id>')
def E_Imper(id):
   imper = db_session.query(models.Impermeabilizante).get(id)
   
   if imper == None:
       flash('ID no encontrado')
       return redirect(url_for('Impers'))
   
   image_paths = [imper.Imagen, imper.IMG2]
    
   base_path = 'static/imagenes/Griferia/Impermeabilizantes'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(imper)
   db_session.commit()
   
   return redirect(url_for('Impers')) 

#---------------- Paneles y Canceles --------------
@app.post('/Add_Panel')
def Add_Panel():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Com = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_PanelCancel'], new_filename))
                return os.path.join(app.config['IMGS_GF_PanelCancel'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_panel = models.Panel_Cancel(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Complementos =Com,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_panel)
    db_session.commit()
    return redirect("Paneles")

@app.post('/Act_Panel/<id>')
def Act_Panel(id):
    panel_act = db_session.query(models.Panel_Cancel).get(id)
       
    if panel_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Paneles'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Com_act = request.form['Complementos_act']

    if panel_act == None:
        flash('No hay nada')
        return redirect (url_for('Paneles'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_PanelCancel'], new_filename))
                return os.path.join(app.config['IMGS_GF_PanelCancel'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    panel_act.Imagen = update_image('Imagen_act', panel_act.Imagen)
    panel_act.IMG2 = update_image('IMG2_act', panel_act.IMG2)
       
    panel_act.Nombre = Name_act
    panel_act.Precio = Prec_act
    panel_act.Codigo = Cod_act
    panel_act.Marca = Marc_act
    panel_act.Color = Col_act
    panel_act.Medida = Med_act
    panel_act.Material = Mat_act
    panel_act.Complementos = Com_act
 
    db_session.add(panel_act)
    db_session.commit()
       
    return redirect(url_for('Paneles'))

@app.get('/E_Panel/<id>')
def E_Panel(id):
   panel = db_session.query(models.Panel_Cancel).get(id)
   
   if panel == None:
       flash('ID no encontrado')
       return redirect(url_for('Paneles'))
   
   image_paths = [panel.Imagen, panel.IMG2]
    
   base_path = 'static/imagenes/Griferia/Panel_Canceles'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(panel)
   db_session.commit()
   
   return redirect(url_for('Paneles'))  

#---------------- Tinas --------------
@app.post('/Add_Tina')
def Add_Tina():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cap = request.form['Capacidad']
    Tip = request.form['Tipo']
    Com = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Tina'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tina'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_tina = models.Tina(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Capacidad =Cap,
        Tipo =Tip,
        Complementos =Com,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_tina)
    db_session.commit()
    return redirect("Tinas")

@app.post('/Act_Tina/<id>')
def Act_Tina(id):
    tina_act = db_session.query(models.Tina).get(id)
       
    if tina_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tinas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Cap_act = request.form['Capacidad_act']
    Tip_act = request.form['Tipo_act']
    Com_act = request.form['Complementos_act']
   
    if tina_act == None:
        flash('No hay nada')
        return redirect (url_for('Tinas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Tina'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tina'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    tina_act.Imagen = update_image('Imagen_act', tina_act.Imagen)
    tina_act.IMG2 = update_image('IMG2_act', tina_act.IMG2)
       
    tina_act.Nombre = Name_act
    tina_act.Precio = Prec_act
    tina_act.Codigo = Cod_act
    tina_act.Marca = Marc_act
    tina_act.Color = Col_act
    tina_act.Medida = Med_act
    tina_act.Material = Mat_act
    tina_act.Capacidad = Cap_act
    tina_act.Tipo = Tip_act
    tina_act.Complementos = Com_act

    db_session.add(tina_act)
    db_session.commit()
       
    return redirect(url_for('Tinas'))

@app.get('/E_Tina/<id>')
def E_Tina(id):
   tina = db_session.query(models.Tina).get(id)
   
   if tina == None:
       flash('ID no encontrado')
       return redirect(url_for('Tinas'))
   
   image_paths = [tina.Imagen, tina.IMG2]
    
   base_path = 'static/imagenes/Griferia/Tinas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(tina)
   db_session.commit()
   
   return redirect(url_for('Tinas'))  

# --------------------------------------- Registro de productos Baños -----------------------------------------
#---------------- Inodoros --------------
@app.post('/Add_Inodoro')
def Add_Inodoro():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Mod = request.form['Modelo']
    Cal = request.form['Calidad']
    Con = request.form['Consumo_agua']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_BN_Inodoro'], new_filename))
                return os.path.join(app.config['IMGS_BN_Inodoro'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_inodoro = models.Inodoro(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Modelo =Mod,
        Calidad =Cal,
        Consumo_agua =Con,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_inodoro)
    db_session.commit()
    return redirect("Inodoros")

@app.post('/Act_Inodoro/<id>')
def Act_Inodoro(id):
    inod_act = db_session.query(models.Inodoro).get(id)
       
    if inod_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Inodoros'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Mod_act = request.form['Modelo_act']
    Cal_act = request.form['Calidad_act']
    Con_act = request.form['Consumo_agua_act']
     
    if inod_act == None:
        flash('No hay nada')
        return redirect (url_for('Inodoros'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_BN_Inodoro'], new_filename))
                return os.path.join(app.config['IMGS_BN_Inodoro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    inod_act.Imagen = update_image('Imagen_act', inod_act.Imagen)
    inod_act.IMG2 = update_image('IMG2_act', inod_act.IMG2)
       
    inod_act.Nombre = Name_act
    inod_act.Precio = Prec_act
    inod_act.Codigo = Cod_act
    inod_act.Marca = Marc_act
    inod_act.Color = Col_act
    inod_act.Medida = Med_act
    inod_act.Material = Mat_act
    inod_act.PrecioAnt = Mod_act
    inod_act.Calidad = Cal_act
    inod_act.Consumo_agua = Con_act

    db_session.add(inod_act)
    db_session.commit()
       
    return redirect(url_for('Inodoros'))

@app.get('/E_Inodoro/<id>')
def E_Inodoro(id):
   inod = db_session.query(models.Inodoro).get(id)
   
   if inod == None:
       flash('ID no encontrado')
       return redirect(url_for('Inodoros'))
   
   image_paths = [inod.Imagen, inod.IMG2]
    
   base_path = 'static/imagenes/Banos/Inodoros/'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(inod)
   db_session.commit()
   
   return redirect(url_for('Inodoros'))

#---------------- Migitorio --------------
@app.post('/Add_Migitorio')
def Add_Migitorio():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Aca = request.form['Acabado']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_BN_Migitorio'], new_filename))
                return os.path.join(app.config['IMGS_BN_Migitorio'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_mig = models.Migitorio(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Acabado =Aca,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_mig)
    db_session.commit()
    return redirect("Migitorios")

@app.post('/Act_Migitorio/<id>')
def Act_Migitorio(id):
    migi_act = db_session.query(models.Migitorio).get(id)
       
    if migi_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Migitorios'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Aca_act = request.form['Acabado_act']

    if migi_act == None:
        flash('No hay nada')
        return redirect (url_for('Migitorios'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_BN_Migitorio'], new_filename))
                return os.path.join(app.config['IMGS_BN_Migitorio'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    migi_act.Imagen = update_image('Imagen_act', migi_act.Imagen)
    migi_act.IMG2 = update_image('IMG2_act', migi_act.IMG2)
       
    migi_act.Nombre = Name_act
    migi_act.Precio = Prec_act
    migi_act.Codigo = Cod_act
    migi_act.Marca = Marc_act
    migi_act.Color = Col_act
    migi_act.Medida = Med_act
    migi_act.Material = Mat_act
    migi_act.Acabado = Aca_act

    db_session.add(migi_act)
    db_session.commit()
       
    return redirect(url_for('Migitorios'))

@app.get('/E_Migitorio/<id>')
def E_Migitorio(id):
   migi = db_session.query(models.Migitorio).get(id)
   
   if migi == None:
       flash('ID no encontrado')
       return redirect(url_for('Migitorios'))
   
   image_paths = [migi.Imagen, migi.IMG2]
    
   base_path = 'static/imagenes/Banos/Migitorios'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(migi)
   db_session.commit()
   
   return redirect(url_for('Migitorios'))  

#---------------- Lavabos --------------
@app.post('/Add_Lavabo')
def Add_Lavabo():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_BN_Lavabo'], new_filename))
                return os.path.join(app.config['IMGS_BN_Lavabo'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_lav = models.Lavabo(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_lav)
    db_session.commit()
    return redirect("Lavabos")

@app.post('/Act_Lavabo/<id>')
def Act_Lavabo(id):
    lava_act = db_session.query(models.Lavabo).get(id)
       
    if lava_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Lavabos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']

    if lava_act == None:
        flash('No hay nada')
        return redirect (url_for('Lavabos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_BN_Lavabo'], new_filename))
                return os.path.join(app.config['IMGS_BN_Lavabo'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    lava_act.Imagen = update_image('Imagen_act', lava_act.Imagen)
    lava_act.IMG2 = update_image('IMG2_act', lava_act.IMG2)
       
    lava_act.Nombre = Name_act
    lava_act.Precio = Prec_act
    lava_act.Codigo = Cod_act
    lava_act.Marca = Marc_act
    lava_act.Color = Col_act
    lava_act.Medida = Med_act
    lava_act.Material = Mat_act

    db_session.add(lava_act)
    db_session.commit()
       
    return redirect(url_for('Lavabos'))

@app.get('/E_Lavabo/<id>')
def E_Lavabo(id):
   lava = db_session.query(models.Lavabo).get(id)
   
   if lava == None:
       flash('ID no encontrado')
       return redirect(url_for('Lavabos'))
   
   image_paths = [lava.Imagen, lava.IMG2]
    
   base_path = 'static/imagenes/Banos/Lavabos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(lava)
   db_session.commit()
   
   return redirect(url_for('Lavabos'))  

#---------------- Kit Sanitarios --------------
@app.post('/Add_Kit_san')
def Add_Kit_san():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cal = request.form['Calidad']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_BN_KitSanitario'], new_filename))
                return os.path.join(app.config['IMGS_BN_KitSanitario'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_kisan = models.Kit_Sanitario(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Calidad =Cal,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_kisan)
    db_session.commit()
    return redirect("Kit_sans")

@app.post('/Act_Kit_san/<id>')
def Act_Kit_san(id):
    kisan_act = db_session.query(models.Kit_Sanitario).get(id)
       
    if kisan_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Kit_sans'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Cal_act = request.form['Calidad_act']
    
    if kisan_act == None:
        flash('No hay nada')
        return redirect (url_for('Kit_sans'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_BN_KitSanitario'], new_filename))
                return os.path.join(app.config['IMGS_BN_KitSanitario'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    kisan_act.Imagen = update_image('Imagen_act', kisan_act.Imagen)
    kisan_act.IMG2 = update_image('IMG2_act', kisan_act.IMG2)
       
    kisan_act.Nombre = Name_act
    kisan_act.Precio = Prec_act
    kisan_act.Codigo = Cod_act
    kisan_act.Marca = Marc_act
    kisan_act.Color = Col_act
    kisan_act.Medida = Med_act
    kisan_act.Material = Mat_act
    kisan_act.Calidad = Cal_act

    db_session.add(kisan_act)
    db_session.commit()
       
    return redirect(url_for('Kit_sans'))

@app.get('/E_Kit_san/<id>')
def E_Kit_san(id):
   kisa = db_session.query(models.Kit_Sanitario).get(id)
   
   if kisa == None:
       flash('ID no encontrado')
       return redirect(url_for('Kit_sans'))
   
   image_paths = [kisa.Imagen, kisa.IMG2]
    
   base_path = 'static/imagenes/Banos/Kit_Sanitarios'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(kisa)
   db_session.commit()
   
   return redirect(url_for('Kit_sans'))  

#---------------- Tinacos --------------
@app.post('/Add_Tinaco')
def Add_Tinaco():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cal = request.form['Calidad']
    Cap = request.form['Capacidad']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_BN_Tinaco'], new_filename))
                return os.path.join(app.config['IMGS_BN_Tinaco'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_tinaco = models.Tinacos(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Calidad =Cal,
        Capacidad =Cap,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_tinaco)
    db_session.commit()
    return redirect("Tinacos")

@app.post('/Act_Tinaco/<id>')
def Act_Tinaco(id):
    tinaco_act = db_session.query(models.Tinacos).get(id)
       
    if tinaco_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tinacos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Cal_act = request.form['Calidad_act']
    Cap_act = request.form['Capacidad_act']

    if tinaco_act == None:
        flash('No hay nada')
        return redirect (url_for('Tinacos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_BN_Tinaco'], new_filename))
                return os.path.join(app.config['IMGS_BN_Tinaco'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    tinaco_act.Imagen = update_image('Imagen_act', tinaco_act.Imagen)
    tinaco_act.IMG2 = update_image('IMG2_act', tinaco_act.IMG2)
       
    tinaco_act.Nombre = Name_act
    tinaco_act.Precio = Prec_act
    tinaco_act.Codigo = Cod_act
    tinaco_act.Marca = Marc_act
    tinaco_act.Color = Col_act
    tinaco_act.Medida = Med_act
    tinaco_act.Material = Mat_act
    tinaco_act.Calidad = Cal_act
    tinaco_act.Capacidad = Cap_act

    db_session.add(tinaco_act)
    db_session.commit()
       
    return redirect(url_for('Tinacos'))

@app.get('/E_Tinaco/<id>')
def E_Tinaco(id):
   tinac = db_session.query(models.Tinacos).get(id)
   
   if tinac == None:
       flash('ID no encontrado')
       return redirect(url_for('Tinacos'))
   
   image_paths = [tinac.Imagen, tinac.IMG2]
    
   base_path = 'static/imagenes/Banos/Tinacos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(tinac)
   db_session.commit()
   
   return redirect(url_for('Tinacos'))






































# ------------------ Respaldo  -----------------------

from flask import Flask, session
from flask import flash
from flask import request
from flask import render_template
from flask import redirect
from werkzeug.security import check_password_hash, generate_password_hash

from flask import render_template
from conexion_db import Database
from conexion_db import engine
from conexion_db import db_session
from flask import url_for
from werkzeug.utils import secure_filename
from functools import wraps

import os   #Se trabaja con archivos y herrameintas del sistema operaivo.
import uuid #Es para que pueda generar ID unicos para cada imagen que se guarde en el sistema, y no haya detahies con que una imagen se repita.
import models
import random

app = Flask(__name__)
app.secret_key = 'UMB[Hola_Israel]13SC191'
Database.metadata.create_all(engine)

# Configuración de carpetas donde se guardarán las imágenes
# ----------------- Pisos y Muros -------------------------
IMGS_PM_Vitro = 'static/imagenes/Pisos_Muros/Vitromex'
app.config['IMGS_PM_Vitro'] = IMGS_PM_Vitro

IMGS_PM_Daltile = 'static/imagenes/Pisos_Muros/Daltile'
app.config['IMGS_PM_Daltile'] = IMGS_PM_Daltile

IMGS_PM_Tecnopiso = 'static/imagenes/Pisos_Muros/Tecnopiso'
app.config['IMGS_PM_Tecnopiso'] = IMGS_PM_Tecnopiso

IMGS_PM_Minato = 'static/imagenes/Pisos_Muros/Minato'
app.config['IMGS_PM_Minato'] = IMGS_PM_Minato

IMGS_PM_Castel = 'static/imagenes/Pisos_Muros/Castel'
app.config['IMGS_PM_Castel'] = IMGS_PM_Castel

IMGS_PM_Cesantoni = 'static/imagenes/Pisos_Muros/Cesantoni'
app.config['IMGS_PM_Cesantoni'] = IMGS_PM_Cesantoni

IMGS_PM_Greda = 'static/imagenes/Pisos_Muros/Greda'
app.config['IMGS_PM_Greda'] = IMGS_PM_Greda

#-------------------- Lo más vendido de las marcas -----------------------
IMGS_Mas_Vitro = 'static/imagenes/Mas_Vend/Vitromex'
app.config['IMGS_Mas_Vitro'] = IMGS_Mas_Vitro

IMGS_Mas_Daltile = 'static/imagenes/Mas_Vend/Daltile/'
app.config['IMGS_Mas_Daltile'] = IMGS_Mas_Daltile

IMGS_Mas_Minato = 'static/imagenes/Mas_Vend/Minato'
app.config['IMGS_Mas_Minato'] = IMGS_Mas_Minato

IMGS_Mas_Castel = 'static/imagenes/Mas_Vend/Castel'
app.config['IMGS_Mas_Castel'] = IMGS_Mas_Castel

IMGS_Mas_Greda = 'static/imagenes/Mas_Vend/Greda'
app.config['IMGS_Mas_Greda'] = IMGS_Mas_Greda

IMGS_Mas_Cesant = 'static/imagenes/Mas_Vend/Cesantoni'
app.config['IMGS_Mas_Cesant'] = IMGS_Mas_Cesant

IMGS_Mas_Tecno = 'static/imagenes/Mas_Vend/Tecnopiso'
app.config['IMGS_Mas_Tecno'] = IMGS_Mas_Tecno

IMGS_Mas_Arko = 'static/imagenes/Mas_Vend/Arko'
app.config['IMGS_Mas_Arko'] = IMGS_Mas_Arko
# ----------------- Grifería -------------------------
IMGS_GF_Perfil = 'static/imagenes/Griferia/Perfiles'
app.config['IMGS_GF_Perfil'] = IMGS_GF_Perfil

IMGS_GF_Cenefa = 'static/imagenes/Griferia/Cenefas'
app.config['IMGS_GF_Cenefa'] = IMGS_GF_Cenefa

IMGS_GF_Malla = 'static/imagenes/Griferia/Mallas'
app.config['IMGS_GF_Malla'] = IMGS_GF_Malla

IMGS_GF_Maneral = 'static/imagenes/Griferia/Manerales'
app.config['IMGS_GF_Maneral'] = IMGS_GF_Maneral

IMGS_GF_Regadera = 'static/imagenes/Griferia/Regaderas'
app.config['IMGS_GF_Regadera'] = IMGS_GF_Regadera

IMGS_GF_Brazo = 'static/imagenes/Griferia/Brazos'
app.config['IMGS_GF_Brazo'] = IMGS_GF_Brazo

IMGS_GF_Tocador = 'static/imagenes/Griferia/Tocadores'
app.config['IMGS_GF_Tocador'] = IMGS_GF_Tocador

IMGS_GF_Parrilla = 'static/imagenes/Griferia/Parrillas'
app.config['IMGS_GF_Parrilla'] = IMGS_GF_Parrilla

IMGS_GF_Campana = 'static/imagenes/Griferia/Campanas'
app.config['IMGS_GF_Campana'] = IMGS_GF_Campana

IMGS_GF_Tarja = 'static/imagenes/Griferia/Tarjas'
app.config['IMGS_GF_Tarja'] = IMGS_GF_Tarja

IMGS_GF_Accesorio = 'static/imagenes/Griferia/Accesorios'
app.config['IMGS_GF_Accesorio'] = IMGS_GF_Accesorio

IMGS_GF_Dispensador = 'static/imagenes/Griferia/Dispensadores'
app.config['IMGS_GF_Dispensador'] = IMGS_GF_Dispensador

IMGS_GF_Mezcladora = 'static/imagenes/Griferia/Mezcladoras'
app.config['IMGS_GF_Mezcladora'] = IMGS_GF_Mezcladora

IMGS_GF_Monomando = 'static/imagenes/Griferia/Monomandos'
app.config['IMGS_GF_Monomando'] = IMGS_GF_Monomando

IMGS_GF_KitInstall = 'static/imagenes/Griferia/KitsInstalls'
app.config['IMGS_GF_KitInstall'] = IMGS_GF_KitInstall

IMGS_GF_Persiana = 'static/imagenes/Griferia/Persianas'
app.config['IMGS_GF_Persiana'] = IMGS_GF_Persiana

IMGS_GF_Organizador = 'static/imagenes/Griferia/Organizadores'
app.config['IMGS_GF_Organizador'] = IMGS_GF_Organizador

IMGS_GF_Asiento = 'static/imagenes/Griferia/Asientos'
app.config['IMGS_GF_Asiento'] = IMGS_GF_Asiento

IMGS_GF_Ovalin = 'static/imagenes/Griferia/Ovalines'
app.config['IMGS_GF_Ovalin'] = IMGS_GF_Ovalin

IMGS_GF_Separador = 'static/imagenes/Griferia/Separadores'
app.config['IMGS_GF_Separador'] = IMGS_GF_Separador

IMGS_GF_HerramientaCol = 'static/imagenes/Griferia/Herramientas_Col'
app.config['IMGS_GF_HerramientaCol'] = IMGS_GF_HerramientaCol

IMGS_GF_CalentadorS = 'static/imagenes/Griferia/Calentadores_S'
app.config['IMGS_GF_CalentadorS'] = IMGS_GF_CalentadorS

IMGS_GF_CalentadorP = 'static/imagenes/Griferia/Calentadores_P'
app.config['IMGS_GF_CalentadorP'] = IMGS_GF_CalentadorP

IMGS_GF_Espejo = 'static/imagenes/Griferia/Espejos'
app.config['IMGS_GF_Espejo'] = IMGS_GF_Espejo

IMGS_GF_Repisa = 'static/imagenes/Griferia/Repisas'
app.config['IMGS_GF_Repisa'] = IMGS_GF_Repisa

IMGS_GF_Resumidero = 'static/imagenes/Griferia/Resumideros'
app.config['IMGS_GF_Resumidero'] = IMGS_GF_Resumidero

IMGS_GF_ContraC = 'static/imagenes/Griferia/Contracanastas'
app.config['IMGS_GF_ContraC'] = IMGS_GF_ContraC

IMGS_GF_Cespol = 'static/imagenes/Griferia/Cespols'
app.config['IMGS_GF_Cespol'] = IMGS_GF_Cespol

IMGS_GF_Impermeabilizante = 'static/imagenes/Griferia/Impermeabilizantes'
app.config['IMGS_GF_Impermeabilizante'] = IMGS_GF_Impermeabilizante

IMGS_GF_PanelCancel = 'static/imagenes/Griferia/Panel_Canceles'
app.config['IMGS_GF_PanelCancel'] = IMGS_GF_PanelCancel

IMGS_GF_Tina = 'static/imagenes/Griferia/Tinas'
app.config['IMGS_GF_Tina'] = IMGS_GF_Tina

#------------------- Baños ------------------------------------

IMGS_BN_Inodoro = 'static/imagenes/Banos/Inodoros'
app.config['IMGS_BN_Inodoro'] = IMGS_BN_Inodoro

IMGS_BN_Migitorio = 'static/imagenes/Banos/Migitorios'
app.config['IMGS_BN_Migitorio'] = IMGS_BN_Migitorio

IMGS_BN_Lavabo = 'static/imagenes/Banos/Lavabos'
app.config['IMGS_BN_Lavabo'] = IMGS_BN_Lavabo

IMGS_BN_KitSanitario = 'static/imagenes/Banos/Kit_Sanitarios'
app.config['IMGS_BN_KitSanitario'] = IMGS_BN_KitSanitario

IMGS_BN_Tinaco = 'static/imagenes/Banos/Tinacos'
app.config['IMGS_BN_Tinaco'] = IMGS_BN_Tinaco

IMGS_BN_Tanque_Est = 'static/imagenes/Banos/Tanques_Est'
app.config['IMGS_BN_Tanque_Est'] = IMGS_BN_Tanque_Est

# -------------------- Ofertas ---------------------------------
IMGS_OFF_PisMur = 'static/imagenes/Ofertas/PM'
app.config['IMGS_OFF_PisMur'] = IMGS_OFF_PisMur

IMGS_OFF_GrifBan = 'static/imagenes/Ofertas/GB'
app.config['IMGS_OFF_GrifBan'] = IMGS_OFF_GrifBan

#Rutas para las vistas de usuarios
@app.get('/')
def home():
    return render_template ('home.html')
# Rutas para los formularios de registro de usuarios

@app.get('/Nuevo_adm') 
def Nuevo_adm():     
    return render_template("/Forms_Add/Add_Admin.html")

@app.get('/Nuevo_sub') 
def Nuevo_sub():   
    return render_template("/Forms_Add/Add_SubAdd.html")

# ---------------------------- Rutas para las vistas de pisos por marca---------------------------------#
@app.get('/Pisos_Vitromex')
def Pisos_Vitromex():
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    return render_template('VitroPisos.html', hola=nombre_usuario, privilegio=privilegio)

@app.get('/Pisos_Daltile')
def Pisos_Daltile():
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    return render_template('DaltaPisos.html', hola=nombre_usuario, privilegio=privilegio)

@app.get('/Pisos_Minato')
def Pisos_Minato():
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    return render_template('MinatoPisos.html', hola=nombre_usuario, privilegio=privilegio)
# ---------------------------- Rutas para los CRUDS de lo más vendido ---------------------------------#
@app.get('/Vitro_Masvend') 
def Vitro_Masvend():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Vitro_masvend = db_session.query(models.Vitro_MasVen).all()
    return render_template("/M_masVend/Vitromex.html", list_product=Vitro_masvend, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Daltile_Masvend') 
def Daltile_Masvend():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Daltile_masvend = db_session.query(models.Daltile_MasVen).all()
    return render_template("/M_masVend/Daltile.html", list_product=Daltile_masvend, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Minato_Masvend') 
def Minato_Masvend():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Minato_masvend = db_session.query(models.Minato_MasVen).all()
    return render_template("/M_masVend/Minato.html", list_product=Minato_masvend, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Castel_Masvend') 
def Castel_Masvend():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Castel_masvend = db_session.query(models.Castel_MasVen).all()
    return render_template("/M_masVend/Castel.html", list_product=Castel_masvend, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Cesant_Masvend') 
def Cesant_Masvend():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Cesant_masvend = db_session.query(models.Cesantoni_MasVen).all()
    return render_template("/M_masVend/Cesantoni.html", list_product=Cesant_masvend, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Tecno_Masvend') 
def Tecno_Masvend():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Tecno_masvend = db_session.query(models.Tecno_MasVen).all()
    return render_template("/M_masVend/Tecnopiso.html", list_product=Tecno_masvend, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Greda_Masvend') 
def Greda_Masvend():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Greda_masvend = db_session.query(models.Greda_MasVen).all()
    return render_template("/M_masVend/Greda.html", list_product=Greda_masvend, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Ark_Masvend') 
def Ark_Masvend():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Arko_masvend = db_session.query(models.Arko_MasVen).all()
    return render_template("/M_masVend/Arko.html", list_product=Arko_masvend, hola=nombre_usuario, privilegio=privilegio)

# ---------------------------- Rutas para los catalogos de lo más vendido ---------------------------------#
@app.get('/Vitromex_Masvend') 
def Vitromex_Masvend():   
    Vitro_masvend = db_session.query(models.Vitro_MasVen).all()
    return render_template("Catalogos/Mas_vendidos/Vitromex.html", list_product=Vitro_masvend)

@app.get('/Dalt_Masvend') 
def Dalt_Masvend():   
    Daltile_masvend = db_session.query(models.Daltile_MasVen).all()
    return render_template("/Catalogos/Mas_vendidos/Daltile.html", list_product=Daltile_masvend)

@app.get('/Mina_Masvend') 
def Mina_Masvend():   
    Minato_masvend = db_session.query(models.Minato_MasVen).all()
    return render_template("/Catalogos/Mas_vendidos/Minato.html", list_product=Minato_masvend)

@app.get('/Cast_Masvend') 
def Cast_Masvend():   
    Castel_masvend = db_session.query(models.Castel_MasVen).all()
    return render_template("/Catalogos/Mas_vendidos/Castel.html", list_product=Castel_masvend)

@app.get('/Cesantoni_Masvend') 
def Cesantoni_Masvend():   
    Cesant_masvend = db_session.query(models.Cesantoni_MasVen).all()
    return render_template("/Catalogos/Mas_vendidos/Cesantoni.html", list_product=Cesant_masvend)

@app.get('/Tecnopiso_Masvend') 
def Tecnopiso_Masvend():   
    Tecno_masvend = db_session.query(models.Tecno_MasVen).all()
    return render_template("/Catalogos/Mas_vendidos/Tecnopiso.html", list_product=Tecno_masvend)

@app.get('/Gred_Masvend') 
def Gred_Masvend():   
    Greda_masvend = db_session.query(models.Greda_MasVen).all()
    return render_template("/Catalogos/Mas_vendidos/Greda.html", list_product=Greda_masvend)

@app.get('/Arko_Masvend') 
def Arko_Masvend():   
    Arko_masvend = db_session.query(models.Arko_MasVen).all()
    return render_template("/Catalogos/Mas_vendidos/Arko.html", list_product=Arko_masvend)

# ---------------------------- Rutas para los CRUDS de pisos vitromex ---------------------------------#
@app.get('/vitroPisos') 
def vitroPisos():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroPiso = db_session.query(models.Vitro_20x20).all()
    return render_template("/VitroPisos/vitro_20x20.html", list_product=vitroPiso, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_20x30') 
def vitro_20x30():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP2030 = db_session.query(models.Vitro_20x30).all()
    return render_template("/VitroPisos/vitro_20x30.html", list_product=vitroP2030, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_30x60') 
def vitro_30x60():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP3060 = db_session.query(models.Vitro_30x60).all()
    return render_template("/VitroPisos/vitro_30x60.html", list_product=vitroP3060, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_36x36') 
def vitro_36x36():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP3636 = db_session.query(models.Vitro_36x36).all()
    return render_template("/VitroPisos/vitro_36x36.html", list_product=vitroP3636, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_36x50') 
def vitro_36x50():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP3650 = db_session.query(models.Vitro_36x50).all()
    return render_template("/VitroPisos/vitro_36x50.html", list_product=vitroP3650, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_37x37') 
def vitro_37x37():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP3737 = db_session.query(models.Vitro_37x37).all()
    return render_template("/VitroPisos/vitro_37x37.html", list_product=vitroP3737, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_45x45') 
def vitro_45x45():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP4545 = db_session.query(models.Vitro_45x45).all()
    return render_template("/VitroPisos/vitro_45x45.html", list_product=vitroP4545, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_50x100') 
def vitro_50x100():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP50100 = db_session.query(models.Vitro_50x100).all()
    return render_template("/VitroPisos/vitro_50x100.html", list_product=vitroP50100, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_55x55') 
def vitro_55x55():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP5555 = db_session.query(models.Vitro_55x55).all()
    return render_template("/VitroPisos/vitro_55x55.html", list_product=vitroP5555, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_60x60') 
def vitro_60x60():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP6060 = db_session.query(models.Vitro_60x60).all()
    return render_template("/VitroPisos/vitro_60x60.html", list_product=vitroP6060, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_60x120') 
def vitro_60x120():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP60120 = db_session.query(models.Vitro_60x120).all()
    return render_template("/VitroPisos/vitro_60x120.html", list_product=vitroP60120, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_61x61') 
def vitro_61x61():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP61x61 = db_session.query(models.Vitro_61x61).all()
    return render_template("/VitroPisos/vitro_61x61.html", list_product=vitroP61x61, hola=nombre_usuario, privilegio=privilegio)

@app.get('/vitro_62x62') 
def vitro_62x62():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroP6262 = db_session.query(models.Vitro_62x62).all()
    return render_template("/VitroPisos/vitro_62x62.html", list_product=vitroP6262, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Vitro_duelas') 
def Vitro_duelas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroPduelas = db_session.query(models.Vitro_duelas).all()
    return render_template("/VitroPisos/vitro_duelas.html", list_product=vitroPduelas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Vitro_otras') 
def Vitro_otras():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    vitroPotra = db_session.query(models.Vitro_otras).all()
    return render_template("/VitroPisos/vitro_otras.html", list_product=vitroPotra, hola=nombre_usuario, privilegio=privilegio)

# ----------------------------------------------- Daltile Pïsos y Muros --------------------------------------

@app.get('/Daltile_30x45') 
def Daltile_30x45():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    dalta3045 = db_session.query(models.Dal_30x45).all()
    return render_template("/DaltaPisos/dal_30x45.html", list_product=dalta3045, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Daltile_37x37') 
def Daltile_37x37():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    dalta3737 = db_session.query(models.Dal_37x37).all()
    return render_template("/DaltaPisos/dal_37x37.html", list_product=dalta3737, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Daltile_45x45') 
def Daltile_45x45():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    dalta4545 = db_session.query(models.Dal_45x45).all()
    return render_template("/DaltaPisos/dal_45x45.html", list_product=dalta4545, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Daltile_60x60') 
def Daltile_60x60():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    dalta6060 = db_session.query(models.Dal_60x60).all()
    return render_template("/DaltaPisos/dal_60x60.html", list_product=dalta6060, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Daltile_duelas') 
def Daltile_duelas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    daltaduelas = db_session.query(models.Dal_duelas).all()
    return render_template("/DaltaPisos/dal_duelas.html", list_product=daltaduelas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Daltile_otras') 
def Daltile_otras():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    daltaotras = db_session.query(models.Dal_otras).all()
    return render_template("/DaltaPisos/dal_otras.html", list_product=daltaotras, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Minato_30x45') 
def Minato_30x45():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    mina3045 = db_session.query(models.Min_30x45).all()
    return render_template("/MinatoPisos/Mina_30x45.html", list_product=mina3045, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Minato_30x60') 
def Minato_30x60():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    mina3060 = db_session.query(models.Min_30x60).all()
    return render_template("/MinatoPisos/Mina_30x60.html", list_product=mina3060, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Minato_60x60') 
def Minato_60x60():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    mina6060 = db_session.query(models.Min_60x60).all()
    return render_template("/MinatoPisos/Mina_60x60.html", list_product=mina6060, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Minato_60x120') 
def Minato_60x120():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    mina60120 = db_session.query(models.Min_60x120).all()
    return render_template("/MinatoPisos/Mina_60x120.html", list_product=mina60120, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Minato_otras') 
def Minato_otras():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    minaotras = db_session.query(models.Min_otras).all()
    return render_template("/MinatoPisos/Mina_otras.html", list_product=minaotras, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Tecno_30x60') 
def Tecno_30x60():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    tecno3060 = db_session.query(models.Tecno_30x60).all()
    return render_template("/TecnoPisos/Tecno_30x60.html", list_product=tecno3060, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Tecno_duelas') 
def Tecno_duelas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    tecnoduela = db_session.query(models.Tecno_duelas).all()
    return render_template("/TecnoPisos/Tecno_duelas.html", list_product=tecnoduela, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Tecno_otras') 
def Tecno_otras():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    tecnootras = db_session.query(models.Tecno_otras).all()
    return render_template("/TecnoPisos/Tecno_otras.html", list_product=tecnootras, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Cesa_30x60') 
def Cesan_30x60():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    cesa3060 = db_session.query(models.Ces_30x60).all()
    return render_template("/CesaPisos/Cesa_30x60.html", list_product=cesa3060, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Cesa_duelas') 
def Cesan_duelas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    cesaduela = db_session.query(models.Ces_duelas).all()
    return render_template("/CesaPisos/Cesa_duelas.html", list_product=cesaduela, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Cesa_otras') 
def Cesan_otras():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    cesaotras = db_session.query(models.Ces_otras).all()
    return render_template("/CesaPisos/Cesa_otras.html", list_product=cesaotras, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Gred_30x45') 
def Gred_30x45():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    gred3045 = db_session.query(models.Gre_30x45).all()
    return render_template("/GredaPisos/Gred_30x45.html", list_product=gred3045, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Gred_30x60') 
def Gred_30x60():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    gred3060 = db_session.query(models.Gre_30x60).all()
    return render_template("/GredaPisos/Gred_30x60.html", list_product=gred3060, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Gred_otras') 
def Gred_otras():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    gredotras = db_session.query(models.Gre_otras).all()
    return render_template("/GredaPisos/Gred_otras.html", list_product=gredotras, hola=nombre_usuario, privilegio=privilegio)


@app.get('/Cast_60x120') 
def Cast_60x120():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Cast60x120 = db_session.query(models.Cast_60x120).all()
    return render_template("/CastelPisos/Cast_60x120.html", list_product=Cast60x120, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Cast_60x60') 
def Cast_60x60():   
    if 'nombre' not in session:
        return redirect(url_for('login'))  # Redirige al login si no está logueado
    nombre_usuario = session['nombre']  # Recupera el nombre del usuario logueado
    Cast60x60 = db_session.query(models.Cast_60x60).all()
    return render_template("/CastelPisos/Cast_60x60.html", list_product=Cast60x60, hola=nombre_usuario)


@app.get('/Cast_duelas') 
def Cast_duelas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    CastDuela = db_session.query(models.Cast_duela).all()
    return render_template("/CastelPisos/Cast_duelas.html", list_product=CastDuela, hola=nombre_usuario, privilegio=privilegio)

#----------------------------- Rutas para las vista de los productos -------------------------

@app.get('/Productos') 
def Productos():   
    productos = db_session.query(models.Productos).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Productos.html", list_product=productos)

@app.get('/Griferia') 
def Griferia():   
    # random.shuffle(productos)
    return render_template("/Catalogos/Griferia.html")

@app.get('/Catalogo_Banos') 
def Catalogo_Banos():   
    # random.shuffle(productos)
    return render_template("/Catalogos/Banos.html")

@app.get('/Catalogo_Ofertas') 
def Catalogo_Ofertas():   
    pisos_Off = db_session.query(models.Pisos_Mur).all()
    GB_Off = db_session.query(models.Grif_Ban).all()
    Ofertas = pisos_Off + GB_Off
    # random.shuffle(Ofertas)
    return render_template("/Catalogos/Ofertas.html", Product_Off=Ofertas)


@app.get('/Catalogo_PM') 
def Catalogo_PM():  
     
    Votras = db_session.query(models.Vitro_otras).all()
    Dotras = db_session.query(models.Dal_otras).all()
    Totras = db_session.query(models.Tecno_otras).all()
    Motras = db_session.query(models.Min_otras).all()
    Cotras = db_session.query(models.Ces_otras).all()
    Gotras = db_session.query(models.Gre_otras).all()
    
    PisMur = Votras + Dotras + Totras + Motras + Cotras + Gotras
    # random.shuffle(productos)
    return render_template("/Catalogos/Pisos_Muros.html", list_product_PM=PisMur)
# ---------------------------- Pisos Vitromex -------------------------------------------
@app.get('/Catalogo_20x20') 
def Catalogo_20x20():   
    C_V20x20 = db_session.query(models.Vitro_20x20).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Pisos/Vitromex/Vitro_20x20.html", list_product_PM=C_V20x20)

@app.get('/Catalogo_36x36') 
def Catalogo_36x36():   
    C_V36x36 = db_session.query(models.Vitro_36x36).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Pisos/Vitromex/Vitro_36x36.html", list_produc_PM=C_V36x36)

@app.get('/Catalogo_37x37') 
def Catalogo_37x37():   
    C_V37x37 = db_session.query(models.Vitro_37x37).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Pisos/Vitromex/Vitro_37x37.html", list_product_PM=C_V37x37)

@app.get('/Catalogo_45x45') 
def Catalogo_45x45():   
    C_V45x45 = db_session.query(models.Vitro_45x45).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Pisos/Vitromex/Vitro_45x45.html", list_product_PM=C_V45x45)

@app.get('/Catalogo_55x55') 
def Catalogo_55x55():   
    C_V55x55 = db_session.query(models.Vitro_55x55).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Pisos/Vitromex/Vitro_55x55.html", list_product_PM=C_V55x55)

@app.get('/Catalogo_60x60') 
def Catalogo_60x60():   
    C_V60x60 = db_session.query(models.Vitro_60x60).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Pisos/Vitromex/Vitro_60x60.html", list_product_PM=C_V60x60)

#--------------------------------- Daltile Pisos ------------------------------------------------

@app.get('/Catalogo_D37x37') 
def Catalogo_D37x37():   
    C_D37x37 = db_session.query(models.Dal_37x37).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Pisos/Daltile/Dal_37x37.html", list_product_PM=C_D37x37)

@app.get('/Catalogo_D45x45') 
def Catalogo_D45x45():   
    C_D45x45 = db_session.query(models.Dal_45x45).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Pisos/Daltile/Dal_45x45.html", list_product_PM=C_D45x45)

@app.get('/Catalogo_D60x60') 
def Catalogo_D60x60():   
    C_D60x60 = db_session.query(models.Dal_60x60).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Pisos/Daltile/Dal_60x60.html", list_product_PM=C_D60x60)

#--------------------------------- Minato Pisos ------------------------------------------------

@app.get('/Catalogo_M60x60') 
def Catalogo_M60x60():   
    C_M60x60 = db_session.query(models.Min_60x60).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Pisos/Minato/Mina_60x60.html", list_product_PM=C_M60x60)

#--------------------------------- Castel Pisos ------------------------------------------------
@app.get('/Catalogo_C60x60') 
def Catalogo_C60x60():   
    C_C60x60 = db_session.query(models.Cast_60x60).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Pisos/Castel/Cast_60x60.html", list_product_PM=C_C60x60)

@app.get('/Catalogo_C60x120') 
def Catalogo_C60x120():   
    C_C60x120 = db_session.query(models.Cast_60x120).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Pisos/Castel/Cast_60x120.html", list_product_PM=C_C60x120)

# ---------------------------- Muros Vitromex -------------------------------------------
@app.get('/Catalogo_20x30') 
def Catalogo_20x30():   
    C_V20x30 = db_session.query(models.Vitro_20x30).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Muros/Vitromex/Vitro_20x30.html", list_product_PM=C_V20x30)

@app.get('/Catalogo_30x60') 
def Catalogo_30x60():   
    C_V30x60 = db_session.query(models.Vitro_30x60).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Muros/Vitromex/Vitro_30x60.html", list_product_PM=C_V30x60)

@app.get('/Catalogo_36x50') 
def Catalogo_36x50():   
    C_V36x50 = db_session.query(models.Vitro_36x50).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Muros/Vitromex/Vitro_36x50.html", list_product_PM=C_V36x50)

@app.get('/Catalogo_50x100') 
def Catalogo_50x100():   
    C_V50x100 = db_session.query(models.Vitro_50x100).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Muros/Vitromex/Vitro_50x100.html", list_product_PM=C_V50x100)

@app.get('/Catalogo_60x120') 
def Catalogo_60x120():   
    C_V60x120 = db_session.query(models.Vitro_60x120).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Muros/Vitromex/Vitro_60x120.html", list_product_PM=C_V60x120)

@app.get('/Catalogo_duelas') 
def Catalogo_duelas():   
    C_Vduelas = db_session.query(models.Vitro_duelas).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Muros/Vitromex/Vitro_duelas.html", list_product_PM=C_Vduelas)

#--------------------------------- Daltile Muros ------------------------------------------------

@app.get('/Catalogo_D30x45') 
def Catalogo_D30x45():   
    C_D30x45 = db_session.query(models.Dal_30x45).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Muros/Daltile/Dal_30x45.html", list_product_PM=C_D30x45)

@app.get('/Catalogo_Dduelas') 
def Catalogo_Dduelas():   
    C_Dduelas = db_session.query(models.Dal_duelas).all()
    # random.shuffle(productos)
    return render_template("/Catalogos/Muros/Daltile/Dal_duelas.html", list_product_PM=C_Dduelas)

#--------------------------------- Minato Muros ------------------------------------------------

@app.get('/Catalogo_M30x45') 
def Catalogo_M30x45():   
    C_M30x45 = db_session.query(models.Min_30x45).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Muros/Minato/Mina_30x45.html", list_product_PM=C_M30x45)

@app.get('/Catalogo_M30x60') 
def Catalogo_M30x60():   
    C_M30x60 = db_session.query(models.Min_30x60).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Muros/Minato/Mina_30x60.html", list_product_PM=C_M30x60)

@app.get('/Catalogo_M60x120') 
def Catalogo_M60x120():   
    C_M60x120 = db_session.query(models.Min_60x120).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Muros/Minato/Mina_60x120.html", list_product_PM=C_M60x120)

#--------------------------------- Cesantoni Muros ------------------------------------------------

@app.get('/Catalogo_Ce30x60') 
def Catalogo_Ce30x60():   
    C_Ce30x60 = db_session.query(models.Ces_30x60).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Muros/Cesantoni/Cesa_30x60.html", list_product_PM=C_Ce30x60)

@app.get('/Catalogo_CeDuelas') 
def Catalogo_CeDuelas():   
    C_Ceduelas = db_session.query(models.Ces_duelas).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Pisos/Cesantoni/Cesa_duelas.html", list_product_PM=C_Ceduelas)

#--------------------------------- Tecnopiso Muros ------------------------------------------------

@app.get('/Catalogo_Te30x60') 
def Catalogo_Te30x60():   
    C_Te30x60 = db_session.query(models.Tecno_30x60).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Muros/Tecnopiso/Tec_30x60.html", list_product_PM=C_Te30x60)

@app.get('/Catalogo_TeDuelas') 
def Catalogo_TeDuelas():   
    C_Teduelas = db_session.query(models.Tecno_duelas).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Pisos/Tecnopiso/Tec_duelas.html", list_product_PM=C_Teduelas)

#--------------------------------- Greda Muros ------------------------------------------------

@app.get('/Catalogo_Gre30x45') 
def Catalogo_Gre30x45():   
    C_Gre30x45 = db_session.query(models.Gre_30x45).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Muros/Greda/Gred_30x45.html", list_product_PM=C_Gre30x45)

@app.get('/Catalogo_Gre30x60') 
def Catalogo_Gre30x60():   
    C_Gre30x60 = db_session.query(models.Gre_30x60).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Muros/Greda/Gred_30x60.html", list_product_PM=C_Gre30x60)
#-----------------------------------------------------------------------------------------------------------

#-------------------------------------- Grifería -----------------------------------------------------------
@app.get('/Cat_AccesoriosB') 
def Cat_AccesoriosB():   
    AccesoriosB = db_session.query(models.Accesorio).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Accesorios_B.html", list_product_Grif=AccesoriosB)

@app.get('/Cat_Asientos') 
def Cat_Asientos():   
    Asientos = db_session.query(models.Asiento).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Asientos.html", list_product_Grif=Asientos)

@app.get('/Cat_Brazos') 
def Cat_Brazos():   
    Brazos = db_session.query(models.Brazo).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Brazos.html", list_product_Grif=Brazos)

@app.get('/Cat_Calentadores_P') 
def Cat_Calentadores_P():   
    Calentadores_P = db_session.query(models.Calentador_P).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/CalentadoresP.html", list_product_Grif=Calentadores_P)


@app.get('/Cat_Calentador_S') 
def Cat_Calentador_S():   
    Calentador_S = db_session.query(models.Calentador_S).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/CalentadoresS.html", list_product_Grif=Calentador_S)

@app.get('/Cat_Campanas') 
def Cat_Campanas():   
    Campanas = db_session.query(models.Campana).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Campanas.html", list_product_Grif=Campanas)

@app.get('/Cat_Cenefas') 
def Cat_Cenefas():   
    Cenefas = db_session.query(models.Cenefa).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Cenefas.html", list_product_Grif=Cenefas)

@app.get('/Cat_Cespols') 
def Cat_Cespols():   
    Cespols = db_session.query(models.Cespol).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Cespols.html", list_product_Grif=Cespols)

@app.get('/Cat_Contracanasta') 
def Cat_Contracanasta():   
    Contracanasta = db_session.query(models.Contra_Can).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/ContraC.html", list_product_Grif=Contracanasta)

@app.get('/Cat_Dispensadores') 
def Cat_Dispensadores():   
    Dispensadores = db_session.query(models.Dispensador).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Dispensadores_J.html", list_product_Grif=Dispensadores)

@app.get('/Cat_Espejos') 
def Cat_Espejos():   
    Espejos = db_session.query(models.Espejo).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Espejos.html", list_product_Grif=Espejos)

@app.get('/Cat_Herramientas_Col') 
def Cat_Herramientas_Col():   
    Herramientas_Col = db_session.query(models.Herramienta_Col).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Herramientas.html", list_product_Grif=Herramientas_Col)

@app.get('/Cat_Impermeabilizantes') 
def Cat_Impermeabilizantes():   
    Impermeabilizantes = db_session.query(models.Impermeabilizante).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Imper.html", list_product_Grif=Impermeabilizantes)

@app.get('/Cat_Kit_Install') 
def Cat_Kit_Install():   
    Kit_Install = db_session.query(models.Kits_install).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Kits_install.html", list_product_Grif=Kit_Install)

@app.get('/Cat_Mallas') 
def Cat_Cat_Mallas():   
    Mallas = db_session.query(models.Maya).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Mallas.html", list_product_Grif=Mallas)

@app.get('/Cat_Manerales') 
def Cat_Cat_Manerales():   
    Manerales = db_session.query(models.Maneral).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Manerales.html", list_product_Grif=Manerales)

@app.get('/Cat_Mezcladoras') 
def Cat_Mezcladoras():   
    Mezcladoras = db_session.query(models.Mezcladora).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Mezcladoras.html", list_product_Grif=Mezcladoras)

@app.get('/Cat_Monomandos') 
def Cat_Monomandos():   
    Monomandos = db_session.query(models.Monomando).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Monomandos.html", list_product_Grif=Monomandos)

@app.get('/Cat_Organizadores') 
def Cat_Organizadores():   
    Organizadores = db_session.query(models.Organizador).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Organizadores.html", list_product_Grif=Organizadores)

@app.get('/Cat_Paneles_Canceles') 
def Cat_Paneles_Canceles():   
    Paneles_Canceles = db_session.query(models.Panel_Cancel).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Paneles.html", list_product_Grif=Paneles_Canceles)

@app.get('/Cat_Parrillas') 
def Cat_Parrillas():   
    Parrillas = db_session.query(models.Parrilla).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Parrillas.html", list_product_Grif=Parrillas)

@app.get('/Cat_Perfiles') 
def Cat_Perfiles():   
    Perfiles = db_session.query(models.Perfil).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Perfiles.html", list_product_Grif=Perfiles)

@app.get('/Cat_Persianas') 
def Cat_Persianas():   
    Persianas = db_session.query(models.Persiana).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Persianas.html", list_product_Grif=Persianas)

@app.get('/Cat_Regaderas') 
def Cat_Regaderas():   
    Regaderas = db_session.query(models.Regadera).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Regaderas.html", list_product_Grif=Regaderas)

@app.get('/Cat_Repisas') 
def Cat_Repisas():   
    Repisas = db_session.query(models.Repisa).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Repisas.html", list_product_Grif=Repisas)

@app.get('/Cat_Resumideros') 
def Cat_Resumideros():   
    Resumideros = db_session.query(models.Resumidero).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Resumideros.html", list_product_Grif=Resumideros)

@app.get('/Cat_Separadores') 
def Cat_Separadores():   
    Separadores = db_session.query(models.Separador).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Separadores.html", list_product_Grif=Separadores)

@app.get('/Cat_Tarjas') 
def Cat_Tarjas():   
    Tarjas = db_session.query(models.Tarja).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Tarjas.html", list_product_Grif=Tarjas)

@app.get('/Cat_Tinas') 
def Cat_Tinas():   
    Tinas = db_session.query(models.Tina).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Griferia/Tinas.html", list_product_Grif=Tinas)


#-------------------------------------------------- Departamento de Baños ------------------------------------------------
@app.get('/Cat_Inodoros') 
def Cat_Inodoros():   
    Cat_Inodoros = db_session.query(models.Inodoro).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Banos/Inodoros.html", list_product_Ban=Cat_Inodoros)

@app.get('/Cat_Kit_san') 
def Cat_Kit_san():   
    Kit_san = db_session.query(models.Kit_Sanitario).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Banos/Kit_san.html", list_product_Ban=Kit_san)

@app.get('/Cat_Lavabos') 
def Cat_Lavabos():   
    Lavabos = db_session.query(models.Lavabo).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Banos/Lavabos.html", list_product_Ban=Lavabos)

@app.get('/Cat_Tinacos') 
def Cat_Tinacos():   
    Tinacos = db_session.query(models.Tinacos).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Banos/Tinacos.html", list_product_Ban=Tinacos)

@app.get('/Cat_Migitorios') 
def Cat_Migitorios():   
    Migitorios = db_session.query(models.Migitorio).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Banos/Migitorios.html", list_product_Ban=Migitorios)

@app.get('/Cat_Ovalines') 
def Cat_Ovalines():   
    Ovalines = db_session.query(models.Ovalin).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Banos/Ovalines.html", list_product_Ban=Ovalines)

@app.get('/Cat_Tocadores') 
def Cat_Tocadores():   
    Tocadores = db_session.query(models.Tocador).all()
    # random.shuffle(productos) 
    return render_template("/Catalogos/Banos/Tocadores.html", list_product_Ban=Tocadores)

# user_type = session['user_type']
#     if user_type == 'administrador':
        # Lógica específica para administrador
    # elif user_type == 'SubAdministrador':
        # Lógica específica para subadministrador

#------------------------------------------------------------------------------------






# ---------------------------- Rutas para las vistas ---------------------------------#
# Consulta de usuarios Administradores
@app.get('/Admins') 
def Admins():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    admins = db_session.query(models.Admin).all()
    return render_template("administradores.html", users=admins, hola=nombre_usuario, privilegio=privilegio)
# Consulta de usuarios subadministradores
@app.get('/subAdmins') 
def subAdmins():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    usuarios = db_session.query(models.SubAdmin).all()
    return render_template("Sub_adm.html", users=usuarios, hola=nombre_usuario, privilegio=privilegio)

@app.get('/griferia')
def griferia():
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    return render_template('Griferia.html', hola=nombre_usuario, privilegio=privilegio)

@app.get('/Banos')
def Banos():
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    return render_template('Banos.html', hola=nombre_usuario, privilegio=privilegio)

@app.get('/perfiles') 
def perfiles():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    perfiles = db_session.query(models.Perfil).all()
    return render_template("/CRUDS_Gif/Perfiles.html", list_perf=perfiles, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Cenefas') 
def Cenefas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    cenefas = db_session.query(models.Cenefa).all()
    return render_template("/CRUDS_Gif/Cenefas.html", list_cen=cenefas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Mallas') 
def Mallas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    mallas = db_session.query(models.Maya).all()
    return render_template("/CRUDS_Gif/Mallas.html", list_mall=mallas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Manerales') 
def Manerales():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    manerales = db_session.query(models.Maneral).all()
    return render_template("/CRUDS_Gif/Manerales.html", list_maneral=manerales, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Regaderas') 
def Regaderas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    regaderas = db_session.query(models.Regadera).all()
    return render_template("/CRUDS_Gif/Regaderas.html", list_reg=regaderas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Brazos') 
def Brazos():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    brazos = db_session.query(models.Brazo).all()
    return render_template("/CRUDS_Gif/Brazos.html", list_braz=brazos, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Tocadores') 
def Tocadores():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    tocadores = db_session.query(models.Tocador).all()
    return render_template("/CRUDS_Gif/Tocadores.html", list_toc=tocadores, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Parrillas') 
def Parrillas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    parrillas = db_session.query(models.Parrilla).all()
    return render_template("/CRUDS_Gif/Parrillas.html", list_parr=parrillas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Campanas') 
def Campanas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    campanas = db_session.query(models.Campana).all()
    return render_template("/CRUDS_Gif/Campanas.html", list_camp=campanas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Tarjas') 
def Tarjas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    tarjas = db_session.query(models.Tarja).all()
    return render_template("/CRUDS_Gif/Tarjas.html", list_tarj=tarjas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Accesorios') 
def Accesorios():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    accesorios = db_session.query(models.Accesorio).all()
    return render_template("/CRUDS_Gif/Accesorios_B.html", list_acces=accesorios, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Dispensadores') 
def Dispensadores():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    dispensadores = db_session.query(models.Dispensador).all()
    return render_template("/CRUDS_Gif/Dispensadores_j.html", list_disp=dispensadores, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Mezcladoras') 
def Mezcladoras():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    mezcladoras = db_session.query(models.Mezcladora).all()
    return render_template("/CRUDS_Gif/Mezcladoras.html", list_mez=mezcladoras, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Monomandos') 
def Monomandos():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    monomandos = db_session.query(models.Monomando).all()
    return render_template("/CRUDS_Gif/Monomandos.html", list_mono=monomandos, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Kits') 
def Kits():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Kits = db_session.query(models.Kits_install).all()
    return render_template("/CRUDS_Gif/Kits_install.html", list_kits=Kits, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Persianas') 
def Persianas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Persianas = db_session.query(models.Persiana).all()
    return render_template("/CRUDS_Gif/Persianas.html", list_pers=Persianas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Organizadores') 
def Organizadores():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    organizadores = db_session.query(models.Organizador).all()
    return render_template("/CRUDS_Gif/Organizadores.html", list_org=organizadores, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Asientos') 
def Asientos():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Asientos = db_session.query(models.Asiento).all()
    return render_template("/CRUDS_Gif/Asientos.html", list_asi=Asientos, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Ovalines') 
def Ovalines():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Ovalines = db_session.query(models.Ovalin).all()
    return render_template("/CRUDS_Gif/Ovalines.html", list_oval=Ovalines, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Separadores') 
def Separadores():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Separadores = db_session.query(models.Separador).all()
    return render_template("/CRUDS_Gif/Separadores.html", list_sep=Separadores, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Herramientas') 
def Herramientas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Herramientas = db_session.query(models.Herramienta_Col).all()
    return render_template("/CRUDS_Gif/Herramientas.html", list_her=Herramientas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/CalentadoresS') 
def CalentadoresS():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    calentadorS = db_session.query(models.Calentador_S).all()
    return render_template("/CRUDS_Gif/CalentadoresS.html", list_cals=calentadorS, hola=nombre_usuario, privilegio=privilegio)

@app.get('/CalentadoresP') 
def CalentadoresP():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    calentadorP = db_session.query(models.Calentador_P).all()
    return render_template("/CRUDS_Gif/CalentadoresP.html", list_calp=calentadorP, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Espejos') 
def Espejos():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Espejos = db_session.query(models.Espejo).all()
    return render_template("/CRUDS_Gif/Espejos.html", list_esp=Espejos, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Repisas') 
def Repisas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Repisas = db_session.query(models.Repisa).all()
    return render_template("/CRUDS_Gif/Repisas.html", list_rep=Repisas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Resumideros') 
def Resumideros():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Resumideros = db_session.query(models.Resumidero).all()
    return render_template("/CRUDS_Gif/Resumideros.html", list_res=Resumideros, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Contracanastas') 
def Contracanastas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Contracanastas = db_session.query(models.Contra_Can).all()
    return render_template("/CRUDS_Gif/ContraC.html", list_contra=Contracanastas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Cespols') 
def Cespols():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Cespols = db_session.query(models.Cespol).all()
    return render_template("/CRUDS_Gif/Cespols.html", list_cesp=Cespols, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Impers') 
def Impers():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Impers = db_session.query(models.Impermeabilizante).all()
    return render_template("/CRUDS_Gif/Imper.html", list_imper=Impers, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Paneles') 
def Paneles():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Paneles = db_session.query(models.Panel_Cancel).all()
    return render_template("/CRUDS_Gif/Paneles.html", list_pan=Paneles, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Tinas') 
def Tinas():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Tinas = db_session.query(models.Tina).all()
    return render_template("/CRUDS_Gif/Tinas.html", list_tin=Tinas, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Inodoros') 
def Inodoros():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Inodoros = db_session.query(models.Inodoro).all()
    return render_template("/CRUDS_Ban/Inodoros.html", list_inod=Inodoros, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Migitorios') 
def Migitorios():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Migitorios = db_session.query(models.Migitorio).all()
    return render_template("/CRUDS_Ban/Migitorios.html", list_mig=Migitorios, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Lavabos') 
def Lavabos():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Lavabos = db_session.query(models.Lavabo).all()
    return render_template("/CRUDS_Ban/Lavabos.html", list_lav=Lavabos, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Kit_sans') 
def Kit_sans():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Kit_sans = db_session.query(models.Kit_Sanitario).all()
    return render_template("/CRUDS_Ban/Kits_san.html", list_kitsa=Kit_sans, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Tinacos') 
def Tinacos():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    tinacos = db_session.query(models.Tinacos).all()
    return render_template("/CRUDS_Ban/Tinacos.html", list_tinac=tinacos, hola=nombre_usuario, privilegio=privilegio)

# ---------------------------------------rutas para las vistas de los depas de PM y GB en Ofertas --------------------

@app.get('/OFF_PM') 
def OFF_PM():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Off_pm = db_session.query(models.Pisos_Mur).all()
    return render_template("/Ofertas/PM/Pisos_Mur.html", list_product=Off_pm, hola=nombre_usuario, privilegio=privilegio)


@app.get('/OFF_GB') 
def OFF_GB():   
    nombre_usuario = session['nombre']
    privilegio = session['privilegio']
    Off_gb = db_session.query(models.Grif_Ban).all()
    return render_template("/Ofertas/GB/Grif_Bans.html", list_product=Off_gb, hola=nombre_usuario, privilegio=privilegio)

@app.get('/Notificacion') 
def Notificacion():   
    hola_sub = session['nombre_sub'] 
    return render_template("/Notificacion.html", hola=hola_sub)

# Rutas para el registro de usuarios en la BD
@app.post('/registrar_admin')
def registrar_admin():
    name = request.form['Nombre']
    Apps = request.form['Apellidos']
    us = request.form['Usuario']
    contra = request.form['Contrasena']
    contraC = request.form['ConfirmarC']
    Priv = request.form['Privilegio']
    
    if contraC == contra:
        nuevo_admin = models.Admin(
        Nombre = name,
        Apellidos = Apps,
        Usuario = us,
        Contrasena =generate_password_hash(contra),
        Privilegio = Priv,
        )
        db_session.add(nuevo_admin)
        db_session.commit()
        flash('Registro exitoso ..!!', 'success')
        return redirect("Nuevo_adm")
    flash('Las contraseñas no coincide ..!!', 'error')
    return redirect("Nuevo_adm")

@app.post('/registrar_subadmin')
def registrar_subadmin():
    name = request.form['Nombre']
    App_P = request.form['Apellido_P']
    us = request.form['Usuario']
    contra = request.form['Contrasena']
    ConfirmC = request.form['ConfirmarC']
    Direc = request.form['Direccion']
    Priv = request.form['Privilegio']
    
    if contra == ConfirmC:
        nuevo_subadmin = models.SubAdmin(
            Nombre = name,
            Apellidos = App_P,
            Usuario = us,
            Contrasena =generate_password_hash(contra),
            Direccion = Direc,
            Privilegio = Priv,
        )
        db_session.add(nuevo_subadmin)
        db_session.commit()
        flash('Registro Exitoso ..!!', 'success')
        return redirect("Nuevo_sub")
    flash('Las contraseñas no coinciden ..!!', 'error')
    return redirect("Nuevo_sub")


@app.get('/admins') #---- Panel de pruebas al reg un new subAdm. 
def admins():   
    admin = db_session.query(models.Admin).all()
    return render_template("administradores.html", lista_admins=admin)

@app.route('/Login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        username = request.form['Usuario']
        password = request.form['password']
        
        # Verificar en la tabla de Administradores   filter_by(Usuario=username).first()
        administrador = db_session.query(models.Admin).filter(models.Admin.Usuario == username).first()
        if administrador and check_password_hash(administrador.Contrasena, password):
            administrador.activo = True
            db_session.commit()
            session['user_id'] = administrador.Id_Admin
            session['nombre'] = administrador.Nombre
            session['privilegio'] = administrador.Privilegio
            session['user_type'] = 'administrador'
            return redirect(url_for('Admin_Panel'))  # Redirige al dashboard del administrador
       
        # Verificar en la tabla de SubAdministradores
        Subadmin = db_session.query(models.SubAdmin).filter(models.SubAdmin.Usuario == username).first()
        if Subadmin and check_password_hash(Subadmin.Contrasena, password):
            Subadmin.activo = True
            db_session.commit()
            session['user_id'] = Subadmin.Id_Sub_Admin
            session['ID_sub'] = Subadmin.Id_Sub_Admin
            session['nombre'] = Subadmin.Usuario
            session['privilegio'] = Subadmin.Privilegio
            session['user_type'] = 'SubAdministrador'
            return redirect(url_for('SubAdmin_Panel'))  # Redirige al dashboard del subadministradores

        flash('Datos incorrectos ..!!')
    
    return render_template('Login.html')

@app.route('/logout', methods=['POST'])
def logout():
    if 'user_id' in session:
        user_id = session['user_id']
        sub_adm = db_session.query(models.SubAdmin).get(user_id)
        Adm = db_session.query(models.Admin).get(user_id)
        if sub_adm:
            sub_adm.activo = False
            db_session.commit()
        if Adm:
            Adm.activo = False
            db_session.commit()
    session.clear()  # Limpia la sesión
    flash('Has cerrado sesión exitosamente.')
    return redirect(url_for('Login'))

def Acceso_requerido(f):
    @wraps(f)
    def Nuevo_decorador(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión para acceder a esta página.')
            return redirect(url_for('Login'))
        return f(*args, **kwargs)
    return Nuevo_decorador

@app.route('/Admin_Panel')
@Acceso_requerido  
def Admin_Panel():
    if 'user_id' in session and session['user_type'] == 'administrador':
        administrador = db_session.query(models.Admin).get(session['user_id'])
        nombre_usuario = session['nombre']
        admin_priv = session['privilegio']
        return redirect("Acceso")
    return redirect(url_for('Login'))
        # return render_template("Panel_Admin.html", hola=nombre_usuario, privilegio=privilegio)

@app.route('/SubAdmin_Panel')
@Acceso_requerido
def SubAdmin_Panel():
    if session['user_type'] == 'SubAdministrador':
        Subadministrador = db_session.query(models.SubAdmin).get(session['user_id'])
        sub_name = session['nombre']
        sub_priv = session['privilegio']
        return redirect("Acceso_S")
    return redirect(url_for('Login'))

# Rutas de acceso
@app.get('/Acceso') 
@Acceso_requerido
def Acceso():   
    nombre_usuario = session['nombre']
    admin_priv = session['privilegio']
    productitos = db_session.query(models.Productos).all()
    return render_template("Panel_Admin.html", list_product = productitos, hola=nombre_usuario, privilegio=admin_priv)

@app.get('/Acceso_S')
@Acceso_requerido 
def Acceso_S(): 
    nombre_usuario = session['nombre']
    sub_priv = session['privilegio']
    productitos = db_session.query(models.Productos).all()
    return render_template("Panel_SubAdmin.html", list_product = productitos, hola=nombre_usuario, privilegio=sub_priv)

# Rutas para el registro de productos en la BD

@app.post('/registro_producto')
def registro_producto():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Marc = request.form['Marca']
    Model = request.form['Modelo']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']


    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')

    nuevo_producto = models.Productos(
        Nombre=Nom,
        Precio=Prec,
        Marca=Marc,
        Modelo=Model,
        Material=Mat,
        Acabado=Acab,
        Color=Col,
        Id_Medida=Medi,
        Contenido=Cont,
        Calidad=Cal,
        Imagen=Img,
        IMG2=Img2,

    )

    db_session.add(nuevo_producto)
    db_session.commit()
    return redirect("Acceso")



# ------------------------------------ Registro de productos de pisos en marca vitromex ------------------------
# Rutas para el registro de productos en pisos de vitro
@app.post('/regVitro_productos')
def regVitro_productos():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    if Medi == '20x20':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_20x20(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2,
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")
    
    elif Medi == '20x30':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_20x30(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")
    
    elif Medi == '30x60':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_30x60(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")
    
    elif Medi == '36x36':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_36x36(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")
    
    elif Medi == '36x50':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_36x50(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")    
    
    elif Medi == '37x37':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_37x37(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")
    
    elif Medi == '45x45':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_45x45(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")
    
    elif Medi == '50x100':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_50x100(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")    
    
    elif Medi == '55x55':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_55x55(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")
    
    elif Medi == '60x60':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_60x60(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")
    
    elif Medi == '60x120':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_60x120(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")    
    
    elif Medi == '61x61':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_61x61(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")
    
    elif Medi == '62x62':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Vitro_62x62(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Vitromex")
    
# -----------------------------------  Vitro duelas  y otras medidas----------------------------------------------    
    
@app.post('/regVitro_duelas')
def regVitro_duelas():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_duela = models.Vitro_duelas(
        Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
    )
    db_session.add(nueva_duela)
    db_session.commit()
    return redirect("Vitro_duelas")


@app.post('/regVitro_otras')
def regVitro_otras():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Vitro_otras(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Vitro_otras")


# Rutas para el registro de productos en pisos de Daltile
@app.post('/regDaltile_productos')
def regDaltile_productos():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    if Medi == '30x45':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Daltile'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Dal_30x45(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Daltile")
    
    elif Medi == '37x37':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Daltile'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Dal_37x37(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Daltile")
    
    elif Medi == '45x45':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Daltile'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Dal_45x45(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Daltile")
    
    elif Medi == '60x60':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Daltile'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Dal_60x60(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Daltile")

# -----------------------------------  Vitro duelas  y otras medidas de Daltile----------------------------------------------        
@app.post('/regDaltile_duelas')
def regDaltile_duelas():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                return os.path.join(app.config['IMGS_PM_Daltile'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_duela = models.Dal_duelas(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
    )
    db_session.add(nueva_duela)
    db_session.commit()
    return redirect("Daltile_duelas")


@app.post('/regDaltile_otras')
def regDaltile_otras():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                return os.path.join(app.config['IMGS_PM_Daltile'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Dal_otras(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Daltile_otras")


# Rutas para el registro de productos en pisos de Minatos
@app.post('/regMinato_productos')
def regMinato_productos():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    if Medi == '30x45':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Minato'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Minato'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Min_30x45(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Minato")
    
    elif Medi == '30x60':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Minato'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Minato'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Min_30x60(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Minato")
    
    elif Medi == '60x120':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Minato'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Minato'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Min_60x120(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Minato")
    
    elif Medi == '60x60':
        def save_image(image_field):
            if image_field:
                file = request.files[image_field]
                if file and file.filename != '':
                    unique_id = str(uuid.uuid4())  # Generar identificador unico
                    filename = secure_filename(file.filename)
                    name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                    new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                    file.save(os.path.join(app.config['IMGS_PM_Minato'], new_filename))
                    return os.path.join(app.config['IMGS_PM_Minato'], new_filename)
            return None

        Img = save_image('Imagen')
        Img2 = save_image('IMG2')
        nuevo_producto = models.Min_60x60(
            Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Id_Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2, 
        )
        db_session.add(nuevo_producto)
        db_session.commit()
        return redirect("Pisos_Minato")

@app.post('/regMin_otras')
def regMin_otras():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Minato'], new_filename))
                return os.path.join(app.config['IMGS_PM_Minato'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Min_otras(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Minato_otras")

# -----------------------------------  Registro de productos en Tecnopiso----------------------------------------------        
@app.post('/regTecno_30x60')
def regTecno_30x60():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename))
                return os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Tecno_30x60(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Tecno_30x60")

@app.post('/regTecno_duelas')
def regTecno_duelas():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename))
                return os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_duela = models.Tecno_duelas(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_duela)
    db_session.commit()
    return redirect("Tecno_duelas")


@app.post('/regTecno_otras')
def regTecno_otras():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename))
                return os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Tecno_otras(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Tecno_otras")


# -----------------------------------  Registro de productos en Cesantoni----------------------------------------------        
@app.post('/regCesa_30x60')
def regCesa_30x60():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename))
                return os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Ces_30x60(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Cesa_30x60")

@app.post('/regCesa_duelas')
def regCesa_duelas():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename))
                return os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_duela = models.Ces_duelas(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_duela)
    db_session.commit()
    return redirect("Cesa_duelas")


@app.post('/regCesa_otras')
def regCesa_otras():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename))
                return os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Ces_otras(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Cesa_otras")

# -----------------------------------  Registro de productos en Castel----------------------------------------------        
@app.post('/regCast_60x60')
def regCast_60x60():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Castel'], new_filename))
                return os.path.join(app.config['IMGS_PM_Castel'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Cast_60x60(
        Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Cast_60x60")


@app.post('/regCast_60x120')
def regCast_60x120():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Castel'], new_filename))
                return os.path.join(app.config['IMGS_PM_Castel'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Cast_60x120(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Cast_60x120")

@app.post('/regCast_duelas')
def regCast_duelas():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Castel'], new_filename))
                return os.path.join(app.config['IMGS_PM_Castel'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_duela = models.Cast_duela(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_duela)
    db_session.commit()
    return redirect("Cast_duelas")


# -----------------------------------  Registro de productos en Greda----------------------------------------------        
@app.post('/regGred_30x45')
def regGred_30x45():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Greda'], new_filename))
                return os.path.join(app.config['IMGS_PM_Greda'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Gre_30x45(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Gred_30x45")

@app.post('/regGred_30x60')
def regGred_30x60():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Greda'], new_filename))
                return os.path.join(app.config['IMGS_PM_Greda'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_duela = models.Gre_30x60(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_duela)
    db_session.commit()
    return redirect("Gred_30x60")


@app.post('/regGred_otras')
def regGred_otras():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_PM_Greda'], new_filename))
                return os.path.join(app.config['IMGS_PM_Greda'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_medida = models.Gre_otras(
         Nombre = Nom,
        Precio = Prec, 
        Codigo = Cod,
        Marca = Marc,
        PrecioAnt = PreA,
        Material = Mat,
        Acabado = Acab,
        Color = Col,
        Id_Medida = Medi,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nueva_medida)
    db_session.commit()
    return redirect("Gred_otras")

# --------------------------------------- Actualizar y eliminar productos VitroPisos -----------------------------------------

@app.post('/Act_VitroP20x20/<id>')
def Act_VitroP20x20(id):
    producto_act = db_session.query(models.Vitro_20x20).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitroPisos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']

    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitroPisos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())  # Generar identificador único
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)  # Separar nombre y extensión
            new_filename = f"{unique_id}_{name}{ext}"  # Renombrar el archivo
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)  # Retornar la ruta completa
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None  # Retornar None si hubo un error pa guardar
        else:
            return None  # Retornar None si no hay archivo subido
    
    # Funcion para guardar la imagen y manejar eliminación de la antiguita
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path)  # Eliminar la imagen antiguita
        return new_image_path if new_image_path else current_image_path

    # Actualizar imágenes si se han subido las nuevas
    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
    
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')   
    return redirect(url_for('vitroPisos'))


@app.get('/E_20x20/<id>')
def E_20x20(id):
   product = db_session.query(models.Vitro_20x20).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitroPisos'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   # Ruta base donde se almacenan las imágenes
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            # Crear la ruta completa de la imagen
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitroPisos')) 


@app.post('/Act_VitroP20x30/<id>')
def Act_VitroP20x30(id):
    producto_act = db_session.query(models.Vitro_20x30).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_20x30'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
       
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_20x30'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
       
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')   
    return redirect(url_for('vitro_20x30'))


@app.get('/E_20x30/<id>')
def E_20x30(id):
   product = db_session.query(models.Vitro_20x30).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_20x30'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   # Ruta base donde se almacenan las imágenes
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            # Crear la ruta completa de la imagen
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_20x30')) 


@app.post('/Act_VitroP30x60/<id>')
def Act_VitroP30x60(id):
    producto_act = db_session.query(models.Vitro_30x60).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_30x60'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
       
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_30x60'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
    
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')   
    return redirect(url_for('vitro_30x60'))


@app.get('/E_30x60/<id>')
def E_30x60(id):
   product = db_session.query(models.Vitro_30x60).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_30x60'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   # Ruta base donde se almacenan las imágenes
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            # Crear la ruta completa de la imagen
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_30x60')) 

@app.post('/Act_VitroP36x36/<id>')
def Act_VitroP36x36(id):
    producto_act = db_session.query(models.Vitro_36x36).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_36x36'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
       
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_36x36'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
    
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
       
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')   
    return redirect(url_for('vitro_36x36'))


@app.get('/E_36x36/<id>')
def E_36x36(id):
   product = db_session.query(models.Vitro_36x36).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_36x36'))
   image_paths = [product.Imagen, product.IMG2]
    
   # Ruta base donde se almacenan las imágenes
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            # Crear la ruta completa de la imagen
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_36x36')) 

@app.post('/Act_VitroP36x50/<id>')
def Act_VitroP36x50(id):
    producto_act = db_session.query(models.Vitro_36x50).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_36x50'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
       
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_36x50'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')   
    return redirect(url_for('vitro_36x50'))


@app.get('/E_36x50/<id>')
def E_36x50(id):
   product = db_session.query(models.Vitro_36x50).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_36x50'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_36x50')) 

@app.post('/Act_VitroP37x37/<id>')
def Act_VitroP37x37(id):
    producto_act = db_session.query(models.Vitro_37x37).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_37x37'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_37x37'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')   
    return redirect(url_for('vitro_37x37'))


@app.get('/E_37x37/<id>')
def E_37x37(id):
   product = db_session.query(models.Vitro_37x37).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_37x37'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_37x37')) 

@app.post('/Act_VitroP45x45/<id>')
def Act_VitroP45x45(id):
    producto_act = db_session.query(models.Vitro_45x45).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_45x45'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_45x45'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act

    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')   
    return redirect(url_for('vitro_45x45'))


@app.get('/E_45x45/<id>')
def E_45x45(id):
   product = db_session.query(models.Vitro_45x45).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_45x45'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_45x45')) 

@app.post('/Act_VitroP50x100/<id>')
def Act_VitroP50x100(id):
    producto_act = db_session.query(models.Vitro_50x100).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_50x100'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
       
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_50x100'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')   
    return redirect(url_for('vitro_50x100'))

@app.get('/E_50x100/<id>')
def E_50x100(id):
   product = db_session.query(models.Vitro_50x100).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_50x100'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_50x100')) 

@app.post('/Act_VitroP55x55/<id>')
def Act_VitroP55x55(id):
    producto_act = db_session.query(models.Vitro_55x55).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_55x55'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_55x55'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('vitro_55x55'))

@app.get('/E_55x55/<id>')
def E_55x55(id):
   product = db_session.query(models.Vitro_55x55).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_55x55'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_55x55')) 

@app.post('/Act_VitroP60x60/<id>')
def Act_VitroP60x60(id):
    producto_act = db_session.query(models.Vitro_60x60).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_60x60'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_60x60'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('vitro_60x60'))

@app.get('/E_60x60/<id>')
def E_60x60(id):
   product = db_session.query(models.Vitro_60x60).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_60x60'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
                
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_60x60')) 


@app.post('/Act_VitroP60x120/<id>')
def Act_VitroP60x120(id):
    producto_act = db_session.query(models.Vitro_60x120).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_60x120'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_60x120'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
       
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('vitro_60x120'))

@app.get('/E_60x120/<id>')
def E_60x120(id):
   product = db_session.query(models.Vitro_60x120).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_60x120'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_60x120')) 

@app.post('/Act_VitroP61x61/<id>')
def Act_VitroP61x61(id):
    producto_act = db_session.query(models.Vitro_61x61).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_61x61'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
       
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_61x61'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('vitro_61x61'))

@app.get('/E_61x61/<id>')
def E_61x61(id):
   product = db_session.query(models.Vitro_61x61).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_61x61'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_61x61')) 


@app.post('/Act_VitroP62x62/<id>')
def Act_VitroP62x62(id):
    producto_act = db_session.query(models.Vitro_62x62).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('vitro_62x62'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('vitro_62x62'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('vitro_62x62'))

@app.get('/E_62x62/<id>')
def E_62x62(id):
   product = db_session.query(models.Vitro_62x62).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('vitro_62x62'))
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
                
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('vitro_62x62')) 
# ---------------------------------------------- Actualizar y eliminar Duelas Vitromex ---------------------------------

@app.post('/Act_VitroPduelas/<id>')
def Act_VitroPduelas(id):
    producto_act = db_session.query(models.Vitro_duelas).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Vitro_duelas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Vitro_duelas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Vitro_duelas'))

@app.get('/E_duelas/<id>')
def E_duelas(id):
   product = db_session.query(models.Vitro_duelas).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Vitro_duelas'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   
   return redirect(url_for('Vitro_duelas')) 

@app.post('/Act_VitroPotras/<id>')
def Act_VitroPotras(id):
    producto_act = db_session.query(models.Vitro_otras).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Vitro_otras'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
       
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Vitro_otras'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
       
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Vitro_otras'))

@app.get('/E_otras/<id>')
def E_otras(id):
   product = db_session.query(models.Vitro_otras).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Vitro_otras'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   
   return redirect(url_for('Vitro_otras')) 
# --------------------------------------- Actualizar y eliminar productos DaltaPisos -----------------------------------------
@app.post('/Act_Dal30x45/<id>')
def Act_Dal30x45(id):
    producto_act = db_session.query(models.Dal_30x45).get(id)
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Daltile_30x45'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Daltile_30x45'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                return os.path.join(app.config['IMGS_PM_Daltile'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
    
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Daltile_30x45'))

@app.get('/E_Dal30x45/<id>')
def E_Dal30x45(id):
   product = db_session.query(models.Dal_30x45).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Daltile_30x45'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Daltile/'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Daltile_30x45')) 


@app.post('/Act_Dal37x37/<id>')
def Act_Dal37x37(id):
    producto_act = db_session.query(models.Dal_37x37).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Daltile_37x37'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Daltile_37x37'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                return os.path.join(app.config['IMGS_PM_Daltile'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Daltile_37x37'))

@app.get('/E_Dal37x37/<id>')
def E_Dal37x37(id):
   product = db_session.query(models.Dal_37x37).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Daltile_37x37'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Daltile/'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Daltile_37x37')) 


@app.post('/Act_Dal45x45/<id>')
def Act_Dal45x45(id):
    producto_act = db_session.query(models.Dal_45x45).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Daltile_45x45'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Daltile_45x45'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                return os.path.join(app.config['IMGS_PM_Daltile'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Daltile_45x45'))


@app.get('/E_Dal45x45/<id>')
def E_Dal45x45(id):
   product = db_session.query(models.Dal_45x45).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Daltile_45x45'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Daltile/'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Daltile_45x45')) 


@app.post('/Act_Dal60x60/<id>')
def Act_Dal60x60(id):
    producto_act = db_session.query(models.Dal_60x60).get(id)
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Daltile_60x60'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Daltile_60x60'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                return os.path.join(app.config['IMGS_PM_Daltile'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
       
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Daltile_60x60'))

@app.get('/E_Dal60x60/<id>')
def E_Dal60x60(id):
   product = db_session.query(models.Dal_60x60).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Daltile_60x60'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Daltile/'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Daltile_60x60')) 

@app.post('/Act_Dalduelas/<id>')
def Act_Dalduelas(id):
    producto_act = db_session.query(models.Dal_duelas).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Daltile_duelas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Daltile_duelas'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                return os.path.join(app.config['IMGS_PM_Daltile'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Daltile_duelas'))

@app.get('/E_Dalduelas/<id>')
def E_Dalduelas(id):
   product = db_session.query(models.Dal_duelas).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Daltile_duelas'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Daltile/'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Daltile_duelas')) 

@app.post('/Act_Dalotras/<id>')
def Act_Dalotras(id):
    producto_act = db_session.query(models.Dal_otras).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Daltile_otras'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Daltile_otras'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Daltile'], new_filename))
                return os.path.join(app.config['IMGS_PM_Daltile'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Daltile_otras'))

@app.get('/E_Dalotras/<id>')
def E_Dalotras(id):
   product = db_session.query(models.Dal_otras).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Daltile_otras'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Daltile/'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Daltile_otras'))
# --------------------------------------- Actualizar y eliminar productos CastPisos -----------------------------------------
@app.post('/Act_Cast_60x60/<id>')
def Act_Cast_60x60(id):
    producto_act = db_session.query(models.Cast_60x60).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cast_60x60'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Cast_60x60'))

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Castel'], new_filename))
                return os.path.join(app.config['IMGS_PM_Castel'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Cast_60x60'))

@app.get('/E_Cast60x60/<id>')
def E_Cast60x60(id):
   product = db_session.query(models.Cast_60x60).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Cast_60x60'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Castel'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Cast_60x60')) 

@app.post('/Act_Cast_60x120/<id>')
def Act_Cast_60x120(id):
    producto_act = db_session.query(models.Cast_60x120).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cast_60x120'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Cast_60x120'))

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Castel'], new_filename))
                return os.path.join(app.config['IMGS_PM_Castel'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Cast_60x120'))

@app.get('/E_Cast60x120/<id>')
def E_Cast60x120(id):
   product = db_session.query(models.Cast_60x120).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Cast_60x120'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Castel'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Cast_60x120')) 

@app.post('/Act_Cast_duelas/<id>')
def Act_Cast_duelas(id):
    producto_act = db_session.query(models.Cast_duela).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cast_duelas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Cast_duelas'))

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Castel'], new_filename))
                return os.path.join(app.config['IMGS_PM_Castel'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Cast_duelas'))

@app.get('/E_Castduelas/<id>')
def E_Castduelas(id):
   product = db_session.query(models.Cast_duela).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Cast_duelas'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Castel'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Cast_duelas')) 
# --------------------------------------- Actualizar y eliminar productos MinaPisos -----------------------------------------
@app.post('/Act_Minato_30x45/<id>')
def Act_Minato_30x45(id):
    producto_act = db_session.query(models.Min_30x45).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Minato_30x45'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Minato_30x45'))

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Minato'], new_filename))
                return os.path.join(app.config['IMGS_PM_Minato'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Minato_30x45'))

@app.get('/E_Min30x45/<id>')
def E_Min30x45(id):
   product = db_session.query(models.Min_30x45).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Minato_30x45'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Minato'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Minato_30x45')) 


@app.post('/Act_Minato_30x60/<id>')
def Act_Minato_30x60(id):
    producto_act = db_session.query(models.Min_30x60).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Minato_30x60'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Minato_30x60'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Minato'], new_filename))
                return os.path.join(app.config['IMGS_PM_Minato'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
    
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Minato_30x60'))

@app.get('/E_Min30x60/<id>')
def E_Min30x60(id):
   product = db_session.query(models.Min_30x60).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Minato_30x60'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Minato'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Minato_30x60')) 


@app.post('/Act_Minato_60x60/<id>')
def Act_Minato_60x60(id):
    producto_act = db_session.query(models.Min_60x60).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Minato_60x60'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Minato_60x60'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Minato'], new_filename))
                return os.path.join(app.config['IMGS_PM_Minato'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Minato_60x60'))


@app.get('/E_Min60x60/<id>')
def E_Min60x60(id):
   product = db_session.query(models.Min_60x60).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Minato_60x60'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Minato'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Minato_60x60')) 

@app.post('/Act_Minato_60x120/<id>')
def Act_Minato_60x120(id):
    producto_act = db_session.query(models.Min_60x120).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Minato_60x120'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Minato_60x120'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Minato'], new_filename))
                return os.path.join(app.config['IMGS_PM_Minato'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Minato_60x120'))

@app.get('/E_Min60x120/<id>')
def E_Min60x120(id):
   product = db_session.query(models.Min_60x120).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Minato_60x120'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Minato'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Minato_60x120')) 

@app.post('/Act_Minato_otras/<id>')
def Act_Minato_otras(id):
    producto_act = db_session.query(models.Min_otras).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Minato_otras'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Minato_otras'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Minato'], new_filename))
                return os.path.join(app.config['IMGS_PM_Minato'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Minato_otras'))

@app.get('/E_Minotras/<id>')
def E_Minotras(id):
   product = db_session.query(models.Min_otras).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Minato_otras'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Minato'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Minato_otras')) 
# --------------------------------------- Actualizar y eliminar productos TecnoPisos -----------------------------------------

@app.post('/Act_Tecno_30x60/<id>')
def Act_Tecno_30x60(id):
    producto_act = db_session.query(models.Tecno_30x60).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tecno_30x60'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Tecno_30x60'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename))
                return os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Tecno_30x60'))

@app.get('/E_T30x60/<id>')
def E_T30x60(id):
   product = db_session.query(models.Tecno_30x60).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Tecno_30x60'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Tecnopiso'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Tecno_30x60')) 

@app.post('/Act_Tecno_duelas/<id>')
def Act_Tecno_duelas(id):
    producto_act = db_session.query(models.Tecno_duelas).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tecno_duelas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Tecno_duelas'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename))
                return os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Tecno_duelas'))

@app.get('/E_Tduelas/<id>')
def E_Tduelas(id):
   product = db_session.query(models.Tecno_duelas).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Tecno_duelas'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Tecnopiso'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Tecno_duelas')) 

@app.post('/Act_Tecno_otras/<id>')
def Act_Tecno_otras(id):
    producto_act = db_session.query(models.Tecno_otras).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tecno_otras'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Tecno_otras'))

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename))
                return os.path.join(app.config['IMGS_PM_Tecnopiso'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Tecno_otras'))

@app.get('/E_Totras/<id>')
def E_Totras(id):
   product = db_session.query(models.Tecno_otras).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Tecno_otras'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Tecnopiso'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Tecno_otras'))

# --------------------------------------- Actualizar y eliminar productos CesaPisos -----------------------------------------
@app.post('/Act_Cesa_30x60/<id>')
def Act_Cesa_30x60(id):
    producto_act = db_session.query(models.Ces_30x60).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cesa_30x60'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Cesan_30x60'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename))
                return os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Cesan_30x60'))

@app.get('/E_Cesa30x60/<id>')
def E_Cesa30x60(id):
   product = db_session.query(models.Ces_30x60).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Cesan_30x60'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Cesantoni'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Cesan_30x60')) 

@app.post('/Act_Cesa_duelas/<id>')
def Act_Cesa_duelas(id):
    producto_act = db_session.query(models.Ces_duelas).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cesan_duelas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Cesan_duelas'))

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename))
                return os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Cesan_duelas'))

@app.get('/E_Cesaduelas/<id>')
def E_Cesaduelas(id):
   product = db_session.query(models.Ces_duelas).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Cesan_duelas'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Cesantoni'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Cesan_duelas')) 

@app.post('/Act_Cesa_otras/<id>')
def Act_Cesa_otras(id):
    producto_act = db_session.query(models.Ces_otras).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cesan_otras'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Cesan_otras'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename))
                return os.path.join(app.config['IMGS_PM_Cesantoni'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Cesan_otras'))


@app.get('/E_Cesaotras/<id>')
def E_Cesaotras(id):
   product = db_session.query(models.Ces_otras).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Cesan_otras'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Cesantoni'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Cesan_otras'))


# --------------------------------------- Actualizar y eliminar productos GredaPisos -----------------------------------------
@app.post('/Act_Gred_30x45/<id>')
def Act_Gred_30x45(id):
    producto_act = db_session.query(models.Gre_30x45).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Gred_30x45'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Gred_30x45'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Greda'], new_filename))
                return os.path.join(app.config['IMGS_PM_Greda'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
    
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Gred_30x45'))

@app.get('/E_Gred30x45/<id>')
def E_Gred30x45(id):
   product = db_session.query(models.Gre_30x45).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Gred_30x45'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Greda'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Gred_30x45')) 

@app.post('/Act_Gred_30x60/<id>')
def Act_Gred_30x60(id):
    producto_act = db_session.query(models.Gre_30x60).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Gred_30x60'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
       
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Gred_30x60'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Greda'], new_filename))
                return os.path.join(app.config['IMGS_PM_Greda'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
    
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
       
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Gred_30x60'))

@app.get('/E_Gred30x60/<id>')
def E_Gred30x60(id):
   product = db_session.query(models.Gre_30x60).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Gred_30x60'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Greda'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Gred_30x60')) 

@app.post('/Act_Gred_otras/<id>')
def Act_Gred_otras(id):
    producto_act = db_session.query(models.Gre_otras).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Gred_otras'))
    
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
       
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('Gred_otras'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_PM_Greda'], new_filename))
                return os.path.join(app.config['IMGS_PM_Greda'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
    
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt=PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Gred_otras'))

@app.get('/E_Gredotras/<id>')
def E_Gredotras(id):
   product = db_session.query(models.Gre_otras).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Gred_otras'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Pisos_Muros/Greda'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Gred_otras'))


# --------------------------------------- Registro de productos Grifería -----------------------------------------
#----------------Perfiles--------------
@app.post('/Add_Perfil')
def Add_Perfil():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Mat = request.form['Material']
    Col = request.form['Color']
    Marc = request.form['Marca']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Perfil'], new_filename))
                return os.path.join(app.config['IMGS_GF_Perfil'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')

    
    nuevo_perfil = models.Perfil(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Material = Mat,
        Color = Col,
        Marca =Marc,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_perfil)
    db_session.commit()
    return redirect("perfiles")

@app.post('/Act_Perfil/<id>')
def Act_Perfil(id):
    perfil_act = db_session.query(models.Perfil).get(id)
       
    if perfil_act == None:
        flash('ID no encontrado')
        return redirect (url_for('perfiles'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Mat_act = request.form['Material_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act'] 
       
    if perfil_act == None:
        flash('No hay nada')
        return redirect (url_for('perfiles'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Perfil'], new_filename))
                return os.path.join(app.config['IMGS_GF_Perfil'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    perfil_act.Imagen = update_image('Imagen_act', perfil_act.Imagen)
    perfil_act.IMG2 = update_image('IMG2_act', perfil_act.IMG2)
    
    perfil_act.Nombre = Name_act
    perfil_act.Precio = Prec_act
    perfil_act.PrecioAnt = PrecAnt_act
    perfil_act.Codigo = Cod_act
    perfil_act.Marca = Marc_act
    perfil_act.Material = Mat_act
    perfil_act.Color = Col_act
    perfil_act.Medida = Med_act
       
    db_session.add(perfil_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('perfiles'))

@app.get('/E_Perfil/<id>')
def E_Perfil(id):
   perfil = db_session.query(models.Perfil).get(id)
   
   if perfil == None:
       flash('ID no encontrado')
       return redirect(url_for('perfiles'))
   
   image_paths = [perfil.Imagen, perfil.IMG2]
    
   base_path = 'static/imagenes/Griferia/Perfiles'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(perfil)
   db_session.commit()
   
   return redirect(url_for('perfiles'))  

#---------------- Cenefas --------------
@app.post('/Add_Cenefa')
def Add_Cenefa():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Cenefa'], new_filename))
                return os.path.join(app.config['IMGS_GF_Cenefa'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_cenefa = models.Cenefa(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_cenefa)
    db_session.commit()
    return redirect("Cenefas")

@app.post('/Act_Cenefa/<id>')
def Act_Cenefa(id):
    cenefa_act = db_session.query(models.Cenefa).get(id)
       
    if cenefa_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cenefas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    
    if cenefa_act == None:
        flash('No hay nada')
        return redirect (url_for('Cenefas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Cenefa'], new_filename))
                return os.path.join(app.config['IMGS_GF_Cenefa'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    cenefa_act.Imagen = update_image('Imagen_act', cenefa_act.Imagen)
    cenefa_act.IMG2 = update_image('IMG2_act', cenefa_act.IMG2)
       
    cenefa_act.Nombre = Name_act
    cenefa_act.Precio = Prec_act
    cenefa_act.Codigo = Cod_act
    cenefa_act.Marca = Marc_act
    cenefa_act.Color = Col_act
    cenefa_act.Medida = Med_act
    cenefa_act.Material = Mat_act
       
    db_session.add(cenefa_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Cenefas'))

@app.get('/E_Cenefa/<id>')
def E_Cenefa(id):
   cenefa = db_session.query(models.Cenefa).get(id)
   
   if cenefa == None:
       flash('ID no encontrado')
       return redirect(url_for('Cenefas'))
   
   image_paths = [cenefa.Imagen, cenefa.IMG2]
   base_path = 'static/imagenes/Griferia/Cenefas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(cenefa)
   db_session.commit()
   
   return redirect(url_for('Cenefas'))  

#---------------- Mallas --------------
@app.post('/Add_Malla')
def Add_Malla():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Malla'], new_filename))
                return os.path.join(app.config['IMGS_GF_Malla'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_malla = models.Maya(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_malla)
    db_session.commit()
    return redirect("Mallas")

@app.post('/Act_Malla/<id>')
def Act_Malla(id):
    malla_act = db_session.query(models.Maya).get(id)
       
    if malla_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Mallas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    
    if malla_act == None:
        flash('No hay nada')
        return redirect (url_for('Mallas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Malla'], new_filename))
                return os.path.join(app.config['IMGS_GF_Malla'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    malla_act.Imagen = update_image('Imagen_act', malla_act.Imagen)
    malla_act.IMG2 = update_image('IMG2_act', malla_act.IMG2)
    
    malla_act.Nombre = Name_act
    malla_act.Precio = Prec_act
    malla_act.Codigo = Cod_act
    malla_act.Marca = Marc_act
    malla_act.Color = Col_act
    malla_act.Medida = Med_act
    malla_act.Material = Mat_act
       
    db_session.add(malla_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Mallas'))

@app.get('/E_Malla/<id>')
def E_Malla(id):
   malla = db_session.query(models.Maya).get(id)
   
   if malla == None:
       flash('ID no encontrado')
       return redirect(url_for('Mallas'))
   
   image_paths = [malla.Imagen, malla.IMG2]
    
   base_path = 'static/imagenes/Griferia/Mallas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(malla)
   db_session.commit()
   
   return redirect(url_for('Mallas'))  

#---------------- Manerales --------------
@app.post('/Add_Maneral')
def Add_Maneral():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Tip_inst = request.form['Tipo_install']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Maneral'], new_filename))
                return os.path.join(app.config['IMGS_GF_Maneral'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_maneral = models.Maneral(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Tipo_install = Tip_inst,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_maneral)
    db_session.commit()
    return redirect("Manerales")

@app.post('/Act_Maneral/<id>')
def Act_Maneral(id):
    maneral_act = db_session.query(models.Maneral).get(id)
       
    if maneral_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Manerales'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Tip_inst_act = request.form['Tipo_install_act']
    
    if maneral_act == None:
        flash('No hay nada')
        return redirect (url_for('Manerales'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Maneral'], new_filename))
                return os.path.join(app.config['IMGS_GF_Maneral'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    maneral_act.Imagen = update_image('Imagen_act', maneral_act.Imagen)
    maneral_act.IMG2 = update_image('IMG2_act', maneral_act.IMG2)
       
    maneral_act.Nombre = Name_act
    maneral_act.Precio = Prec_act
    maneral_act.Codigo = Cod_act
    maneral_act.Marca = Marc_act
    maneral_act.Color = Col_act
    maneral_act.Material = Mat_act
    maneral_act.Tipo_install = Tip_inst_act
       
    db_session.add(maneral_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Manerales'))

@app.get('/E_Maneral/<id>')
def E_Maneral(id):
   maneral = db_session.query(models.Maneral).get(id)
   
   if maneral == None:
       flash('ID no encontrado')
       return redirect(url_for('Manerales'))
   
   image_paths = [maneral.Imagen, maneral.IMG2]
    
   base_path = 'static/imagenes/Griferia/Manerales'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(maneral)
   db_session.commit()
   
   return redirect(url_for('Manerales'))  

#---------------- Regaderas --------------
@app.post('/Add_Regadera')
def Add_Regadera():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Flu = request.form['Flujo_agua']
    Presion = request.form['Presion']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Regadera'], new_filename))
                return os.path.join(app.config['IMGS_GF_Regadera'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_regadera = models.Regadera(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Flujo_agua =Flu,
        Presion =Presion,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_regadera)
    db_session.commit()
    return redirect("Regaderas")

@app.post('/Act_Regadera/<id>')
def Act_Regadera(id):
    regadera_act = db_session.query(models.Regadera).get(id)
       
    if regadera_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Regaderas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Flu_act = request.form['Flujo_agua_act']
    Presi_act = request.form['Presion_act']
    
    if regadera_act == None:
        flash('No hay nada')
        return redirect (url_for('Regaderas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Regadera'], new_filename))
                return os.path.join(app.config['IMGS_GF_Regadera'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    regadera_act.Imagen = update_image('Imagen_act', regadera_act.Imagen)
    regadera_act.IMG2 = update_image('IMG2_act', regadera_act.IMG2)
       
    regadera_act.Nombre = Name_act
    regadera_act.Precio = Prec_act
    regadera_act.Codigo = Cod_act
    regadera_act.Marca = Marc_act
    regadera_act.Color = Col_act
    regadera_act.Medida = Med_act
    regadera_act.Material = Mat_act
    regadera_act.Flujo_agua = Flu_act
    regadera_act.Presion = Presi_act
       
    db_session.add(regadera_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Regaderas'))

@app.get('/E_Regadera/<id>')
def E_Regadera(id):
   regadera = db_session.query(models.Regadera).get(id)
   
   if regadera == None:
       flash('ID no encontrado')
       return redirect(url_for('Regaderas'))
   
   image_paths = [regadera.Imagen, regadera.IMG2]
    
   base_path = 'static/imagenes/Griferia/Regaderas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(regadera)
   db_session.commit()
   
   return redirect(url_for('Regaderas'))  

#---------------- Brazos --------------
@app.post('/Add_Brazo')
def Add_Brazo():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Flu = request.form['Flujo_agua']
    Presion = request.form['Presion']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Brazo'], new_filename))
                return os.path.join(app.config['IMGS_GF_Brazo'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_brazo = models.Brazo(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Flujo_agua =Flu,
        Presion =Presion,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_brazo)
    db_session.commit()
    return redirect("Brazos")

@app.post('/Act_Brazo/<id>')
def Act_Brazo(id):
    brazo_act = db_session.query(models.Brazo).get(id)
       
    if brazo_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Brazos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Flu_act = request.form['Flujo_agua_act']
    Presi_act = request.form['Presion_act']

    if brazo_act == None:
        flash('No hay nada')
        return redirect (url_for('Brazos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Brazo'], new_filename))
                return os.path.join(app.config['IMGS_GF_Brazo'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    brazo_act.Imagen = update_image('Imagen_act', brazo_act.Imagen)
    brazo_act.IMG2 = update_image('IMG2_act', brazo_act.IMG2)
       
    brazo_act.Nombre = Name_act
    brazo_act.Precio = Prec_act
    brazo_act.Codigo = Cod_act
    brazo_act.Marca = Marc_act
    brazo_act.Color = Col_act
    brazo_act.Medida = Med_act
    brazo_act.Material = Mat_act
    brazo_act.Flujo_agua = Flu_act
    brazo_act.Presion = Presi_act
       
    db_session.add(brazo_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Brazos'))

@app.get('/E_Brazo/<id>')
def E_Brazo(id):
   brazos = db_session.query(models.Brazo).get(id)
   
   if brazos == None:
       flash('ID no encontrado')
       return redirect(url_for('Brazos'))
   
   image_paths = [brazos.Imagen, brazos.IMG2]
    
   base_path = 'static/imagenes/Griferia/Brazos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(brazos)
   db_session.commit()
   
   return redirect(url_for('Brazos')) 

#---------------- Tocadores --------------
@app.post('/Add_Tocador')
def Add_Tocador():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Tocador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tocador'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_tocador = models.Tocador(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_tocador)
    db_session.commit()
    return redirect("Tocadores")

@app.post('/Act_Tocador/<id>')
def Act_Tocador(id):
    tocador_act = db_session.query(models.Tocador).get(id)
       
    if tocador_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tocadores'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']

    if tocador_act == None:
        flash('No hay nada')
        return redirect (url_for('Tocadores'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Tocador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tocador'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    tocador_act.Imagen = update_image('Imagen_act', tocador_act.Imagen)
    tocador_act.IMG2 = update_image('IMG2_act', tocador_act.IMG2)
       
    tocador_act.Nombre = Name_act
    tocador_act.Precio = Prec_act
    tocador_act.Codigo = Cod_act
    tocador_act.Marca = Marc_act
    tocador_act.Color = Col_act
    tocador_act.Medida = Med_act
    tocador_act.Material = Mat_act
       
    db_session.add(tocador_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Tocadores'))

@app.get('/E_Tocador/<id>')
def E_Tocador(id):
   tocador = db_session.query(models.Tocador).get(id)
   
   if tocador == None:
       flash('ID no encontrado')
       return redirect(url_for('Tocadores'))
   
   image_paths = [tocador.Imagen, tocador.IMG2]
    
   base_path = 'static/imagenes/Griferia/Tocadores'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(tocador)
   db_session.commit()
   
   return redirect(url_for('Tocadores'))  

#---------------- Parrillas --------------
@app.post('/Add_Parrilla')
def Add_Parrilla():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Comp = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Parrilla'], new_filename))
                return os.path.join(app.config['IMGS_GF_Parrilla'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_parrilla = models.Parrilla(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Complementos =Comp,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_parrilla)
    db_session.commit()
    return redirect("Parrillas")

@app.post('/Act_Parrilla/<id>')
def Act_Parrilla(id):
    parrilla_act = db_session.query(models.Parrilla).get(id)
       
    if parrilla_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Parrillas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Comp_act = request.form['Complementos_act']
    
    if parrilla_act == None:
        flash('No hay nada')
        return redirect (url_for('Parrillas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Parrilla'], new_filename))
                return os.path.join(app.config['IMGS_GF_Parrilla'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    parrilla_act.Imagen = update_image('Imagen_act', parrilla_act.Imagen)
    parrilla_act.IMG2 = update_image('IMG2_act', parrilla_act.IMG2)
       
    parrilla_act.Nombre = Name_act
    parrilla_act.Precio = Prec_act
    parrilla_act.Codigo = Cod_act
    parrilla_act.Marca = Marc_act
    parrilla_act.Color = Col_act
    parrilla_act.Medida = Med_act
    parrilla_act.Material = Mat_act
    parrilla_act.Complementos = Comp_act
       
    db_session.add(parrilla_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Parrillas'))

@app.get('/E_Parrilla/<id>')
def E_Parrilla(id):
   parrilla = db_session.query(models.Parrilla).get(id)
   
   if parrilla == None:
       flash('ID no encontrado')
       return redirect(url_for('Parrillas'))
   
   image_paths = [parrilla.Imagen, parrilla.IMG2]
    
   base_path = 'static/imagenes/Griferia/Parrillas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(parrilla)
   db_session.commit()
   
   return redirect(url_for('Parrillas'))  

#---------------- Campanas --------------
@app.post('/Add_Campana')
def Add_Campana():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Comp = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Campana'], new_filename))
                return os.path.join(app.config['IMGS_GF_Campana'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_campana = models.Campana(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Complementos =Comp,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_campana)
    db_session.commit()
    return redirect("Campanas")

@app.post('/Act_Campana/<id>')
def Act_Campana(id):
    campana_act = db_session.query(models.Campana).get(id)
       
    if campana_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Campanas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Comp_act = request.form['Complementos_act']
    
    if campana_act == None:
        flash('No hay nada')
        return redirect (url_for('Campanas'))
       
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Campana'], new_filename))
                return os.path.join(app.config['IMGS_GF_Campana'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    campana_act.Imagen = update_image('Imagen_act', campana_act.Imagen)
    campana_act.IMG2 = update_image('IMG2_act', campana_act.IMG2)
    
    campana_act.Nombre = Name_act
    campana_act.Precio = Prec_act
    campana_act.Codigo = Cod_act
    campana_act.Marca = Marc_act
    campana_act.Color = Col_act
    campana_act.Medida = Med_act
    campana_act.Material = Mat_act
    campana_act.Complementos = Comp_act
       
    db_session.add(campana_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Campanas'))

@app.get('/E_Campana/<id>')
def E_Campana(id):
   campana = db_session.query(models.Campana).get(id)
   
   if campana == None:
       flash('ID no encontrado')
       return redirect(url_for('Campanas'))
   
   image_paths = [campana.Imagen, campana.IMG2]
    
   base_path = 'static/imagenes/Griferia/Campanas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(campana)
   db_session.commit()
   
   return redirect(url_for('Campanas')) 

#---------------- Tarjas --------------
@app.post('/Add_Tarja')
def Add_Tarja():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Tarja'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tarja'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_tarja = models.Tarja(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_tarja)
    db_session.commit()
    return redirect("Tarjas")

@app.post('/Act_Tarja/<id>')
def Act_Tarja(id):
    tarja_act = db_session.query(models.Tarja).get(id)
       
    if tarja_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tarjas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
       
    if tarja_act == None:
        flash('No hay nada')
        return redirect (url_for('Tarjas'))
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Tarja'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tarja'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    tarja_act.Imagen = update_image('Imagen_act', tarja_act.Imagen)
    tarja_act.IMG2 = update_image('IMG2_act', tarja_act.IMG2)
       
    tarja_act.Nombre = Name_act
    tarja_act.Precio = Prec_act
    tarja_act.Codigo = Cod_act
    tarja_act.Marca = Marc_act
    tarja_act.Color = Col_act
    tarja_act.Medida = Med_act
    tarja_act.Material = Mat_act
       
    db_session.add(tarja_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Tarjas'))

@app.get('/E_Tarja/<id>')
def E_Tarja(id):
   tarja = db_session.query(models.Tarja).get(id)
   
   if tarja == None:
       flash('ID no encontrado')
       return redirect(url_for('Tarjas'))
   
   image_paths = [tarja.Imagen, tarja.IMG2]
    
   base_path = 'static/imagenes/Griferia/Tarjas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(tarja)
   db_session.commit()
   
   return redirect(url_for('Tarjas')) 

#---------------- Accesorios --------------
@app.post('/Add_Accesorio')
def Add_Accesorio():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Com = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Accesorio'], new_filename))
                return os.path.join(app.config['IMGS_GF_Accesorio'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_accesorio = models.Accesorio(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Complementos = Com,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_accesorio)
    db_session.commit()
    return redirect("Accesorios")

@app.post('/Act_Accesorio/<id>')
def Act_Accesorio(id):
    acceso_act = db_session.query(models.Accesorio).get(id)
       
    if acceso_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Accesorios'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Com_act = request.form['Complementos_act']
    
    if acceso_act == None:
        flash('No hay nada')
        return redirect (url_for('Accesorios'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Accesorio'], new_filename))
                return os.path.join(app.config['IMGS_GF_Accesorio'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    acceso_act.Imagen = update_image('Imagen_act', acceso_act.Imagen)
    acceso_act.IMG2 = update_image('IMG2_act', acceso_act.IMG2)
       
    acceso_act.Nombre = Name_act
    acceso_act.Precio = Prec_act
    acceso_act.Codigo = Cod_act
    acceso_act.Marca = Marc_act
    acceso_act.Color = Col_act
    acceso_act.Material = Mat_act
    acceso_act.Complementos = Com_act

    db_session.add(acceso_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Accesorios'))

@app.get('/E_Accesorio/<id>')
def E_Accesorio(id):
   acceso = db_session.query(models.Accesorio).get(id)
   
   if acceso == None:
       flash('ID no encontrado')
       return redirect(url_for('Accesorios'))
   
   image_paths = [acceso.Imagen, acceso.IMG2]
    
   base_path = 'static/imagenes/Griferia/Accesorios'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(acceso)
   db_session.commit()
   
   return redirect(url_for('Accesorios')) 

#---------------- Dispensadores --------------
@app.post('/Add_Dispensador')
def Add_Dispensador():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cap = request.form['Capacidad']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Dispensador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Dispensador'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_dispensador = models.Dispensador(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Capacidad = Cap,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_dispensador)
    db_session.commit()
    return redirect("Dispensadores")

@app.post('/Act_Dispensador/<id>')
def Act_Dispensador(id):
    dispen_act = db_session.query(models.Dispensador).get(id)
       
    if dispen_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Dispensadores'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Cap_act = request.form['Capacidad_act']

    if dispen_act == None:
        flash('No hay nada')
        return redirect (url_for('Dispensadores'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Dispensador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Dispensador'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    dispen_act.Imagen = update_image('Imagen_act', dispen_act.Imagen)
    dispen_act.IMG2 = update_image('IMG2_act', dispen_act.IMG2)
       
    dispen_act.Nombre = Name_act
    dispen_act.Precio = Prec_act
    dispen_act.Codigo = Cod_act
    dispen_act.Marca = Marc_act
    dispen_act.Color = Col_act
    dispen_act.Material = Mat_act
    dispen_act.Capacidad = Cap_act
       
    db_session.add(dispen_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Dispensadores'))

@app.get('/E_Dispensador/<id>')
def E_Dispensador(id):
   dispe = db_session.query(models.Dispensador).get(id)
   
   if dispe == None:
       flash('ID no encontrado')
       return redirect(url_for('Dispensadores'))
   
   image_paths = [dispe.Imagen, dispe.IMG2]
    
   base_path = 'static/imagenes/Griferia/Dispensadores'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(dispe)
   db_session.commit()
   
   return redirect(url_for('Dispensadores')) 

#---------------- Mezcladoras --------------
@app.post('/Add_Mezcladora')
def Add_Mezcladora():
    Name = request.form['Nombre']
    PreC = request.form['Precio']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Pre = request.form['Presion']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Mezcladora'], new_filename))
                return os.path.join(app.config['IMGS_GF_Mezcladora'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_mezcla = models.Mezcladora(
        Nombre = Name,
        Precio = PreC,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Presion = Pre,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_mezcla)
    db_session.commit()
    return redirect("Mezcladoras")

@app.post('/Act_Mezcladora/<id>')
def Act_Mezcladora(id):
    mezcla_act = db_session.query(models.Mezcladora).get(id)
       
    if mezcla_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Mezcladoras'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Pre_act = request.form['Presion_act']
    
    if mezcla_act == None:
        flash('No hay nada')
        return redirect (url_for('Mezcladoras'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Mezcladora'], new_filename))
                return os.path.join(app.config['IMGS_GF_Mezcladora'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    mezcla_act.Imagen = update_image('Imagen_act', mezcla_act.Imagen)
    mezcla_act.IMG2 = update_image('IMG2_act', mezcla_act.IMG2)
       
    mezcla_act.Nombre = Name_act
    mezcla_act.Precio = Prec_act
    mezcla_act.Codigo = Cod_act
    mezcla_act.Marca = Marc_act
    mezcla_act.Color = Col_act
    mezcla_act.Material = Mat_act
    mezcla_act.Presion = Pre_act

    db_session.add(mezcla_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Mezcladoras'))

@app.get('/E_Mezcladora/<id>')
def E_Mezcladora(id):
   mezcla = db_session.query(models.Mezcladora).get(id)
   
   if mezcla == None:
       flash('ID no encontrado')
       return redirect(url_for('Mezcladoras'))
   
   image_paths = [mezcla.Imagen, mezcla.IMG2]
    
   base_path = 'static/imagenes/Griferia/Mezcladoras'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(mezcla)
   db_session.commit()
   
   return redirect(url_for('Mezcladoras')) 

#---------------- Monomandos --------------
@app.post('/Add_Monomando')
def Add_Monomando():
    Name = request.form['Nombre']
    Prec = request.form['Precio']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Pre = request.form['Presion']
    Comp = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Monomando'], new_filename))
                return os.path.join(app.config['IMGS_GF_Monomando'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_mono = models.Monomando(
        Nombre = Name,
        Precio = Prec,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Presion = Pre,
        Complementos = Comp,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_mono)
    db_session.commit()
    return redirect("Monomandos")

@app.post('/Act_Monomando/<id>')
def Act_Monomando(id):
    mono_act = db_session.query(models.Monomando).get(id)
       
    if mono_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Monomandos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Pre_act = request.form['Presion_act']
    Comp_act = request.form['Complementos_act']
       
    if mono_act == None:
        flash('No hay nada')
        return redirect (url_for('Monomandos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Monomando'], new_filename))
                return os.path.join(app.config['IMGS_GF_Monomando'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    mono_act.Imagen = update_image('Imagen_act', mono_act.Imagen)
    mono_act.IMG2 = update_image('IMG2_act', mono_act.IMG2)
       
    mono_act.Nombre = Name_act
    mono_act.Precio = Prec_act
    mono_act.Codigo = Cod_act
    mono_act.Marca = Marc_act
    mono_act.Color = Col_act
    mono_act.Material = Mat_act
    mono_act.Presion = Pre_act
    mono_act.Complementos = Comp_act

    db_session.add(mono_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Monomandos'))

@app.get('/E_Monomando/<id>')
def E_Monomando(id):
   mono = db_session.query(models.Monomando).get(id)
   
   if mono == None:
       flash('ID no encontrado')
       return redirect(url_for('Monomandos'))
   
   image_paths = [mono.Imagen, mono.IMG2]
    
   base_path = 'static/imagenes/Griferia/Monomandos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(mono)
   db_session.commit()
   
   return redirect(url_for('Monomandos')) 

#---------------- Kits de instalación --------------
@app.post('/Add_Kit')
def Add_Kit():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med_ll = request.form['Medida_llaves']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Contra = request.form['Contracanasta']
    Ali = request.form['Alimentador']
    Comp = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_KitInstall'], new_filename))
                return os.path.join(app.config['IMGS_GF_KitInstall'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_kit = models.Kits_install(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida_llaves = Med_ll,
        Marca =Marc,
        Material =Mat,
        Contracanasta = Contra,
        Alimentador = Ali,
        Complementos = Comp,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_kit)
    db_session.commit()
    return redirect("Kits")

@app.post('/Act_Kit/<id>')
def Act_Kit(id):
    kit_act = db_session.query(models.Kits_install).get(id)
       
    if kit_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Kits'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Med_ll_act = request.form['Medida_llaves_act']
    Mat_act = request.form['Material_act']
    Contra_act = request.form['Contracanasta_act']
    Ali_act = request.form['Alimentador_act']
    Comp_act = request.form['Complementos_act']

    if kit_act == None:
        flash('No hay nada')
        return redirect (url_for('Kits'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_KitInstall'], new_filename))
                return os.path.join(app.config['IMGS_GF_KitInstall'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    kit_act.Imagen = update_image('Imagen_act', kit_act.Imagen)
    kit_act.IMG2 = update_image('IMG2_act', kit_act.IMG2)
       
    kit_act.Nombre = Name_act
    kit_act.Precio = Prec_act
    kit_act.Codigo = Cod_act
    kit_act.Marca = Marc_act
    kit_act.Medida_llaves = Med_ll_act
    kit_act.Material = Mat_act
    kit_act.Contracanasta = Contra_act
    kit_act.Alimentador = Ali_act
    kit_act.Complementos = Comp_act

    db_session.add(kit_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Kits'))

@app.get('/E_Kit/<id>')
def E_Kit(id):
   kit = db_session.query(models.Kits_install).get(id)
   
   if kit == None:
       flash('ID no encontrado')
       return redirect(url_for('Kits'))
   
   image_paths = [kit.Imagen, kit.IMG2]
    
   base_path = 'static/imagenes/Griferia/KitsInstalls'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(kit)
   db_session.commit()
   
   return redirect(url_for('Kits')) 

#---------------- Persianas --------------
@app.post('/Add_Persiana')
def Add_Persiana():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Comp = request.form['Complementos']
    Tiem = request.form['Tiempo_entrega']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Persiana'], new_filename))
                return os.path.join(app.config['IMGS_GF_Persiana'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_persiana = models.Persiana(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Tiempo_entrega = Tiem,
        Complementos = Comp,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_persiana)
    db_session.commit()
    return redirect("Persianas")

@app.post('/Act_Persiana/<id>')
def Act_Persiana(id):
    persi_act = db_session.query(models.Persiana).get(id)
       
    if persi_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Persianas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Comp_act = request.form['Complementos_act']
    Tiem_act = request.form['Tiempo_entrega_act']

    if persi_act == None:
        flash('No hay nada')
        return redirect (url_for('Persianas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Persiana'], new_filename))
                return os.path.join(app.config['IMGS_GF_Persiana'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    persi_act.Imagen = update_image('Imagen_act', persi_act.Imagen)
    persi_act.IMG2 = update_image('IMG2_act', persi_act.IMG2)
       
    persi_act.Nombre = Name_act
    persi_act.Precio = Prec_act
    persi_act.Codigo = Cod_act
    persi_act.Marca = Marc_act
    persi_act.Color = Col_act
    persi_act.Material = Mat_act
    persi_act.Complementos = Comp_act
    persi_act.Tiempo_entrega = Tiem_act
       
    db_session.add(persi_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Persianas'))

@app.get('/E_Persiana/<id>')
def E_Persiana(id):
   persi = db_session.query(models.Persiana).get(id)
   
   if persi == None:
       flash('ID no encontrado')
       return redirect(url_for('Persianas'))
   
   image_paths = [persi.Imagen, persi.IMG2]
    
   base_path = 'static/imagenes/Griferia/Persianas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(persi)
   db_session.commit()
   
   return redirect(url_for('Persianas')) 
#---------------- Organizadores --------------
@app.post('/Add_hola')
def Add_Organizador():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Organizador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Organizador'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_orga = models.Organizador(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_orga)
    db_session.commit()
    return redirect("Organizadores")

@app.post('/Act_Organizador/<id>')
def Act_Organizador(id):
    orga_act = db_session.query(models.Organizador).get(id)
    if orga_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Organizadores'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
       
    if orga_act == None:
        flash('No hay nada')
        return redirect (url_for('Organizadores'))
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Organizador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Organizador'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    orga_act.Imagen = update_image('Imagen_act', orga_act.Imagen)
    orga_act.IMG2 = update_image('IMG2_act', orga_act.IMG2)
       
    orga_act.Nombre = Name_act
    orga_act.Precio = Prec_act
    orga_act.Codigo = Cod_act
    orga_act.Marca = Marc_act
    orga_act.Color = Col_act
    orga_act.Medida = Med_act
    orga_act.Material = Mat_act

    db_session.add(orga_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Organizadores'))

@app.get('/E_Organizador/<id>')
def E_Organizador(id):
   orga = db_session.query(models.Organizador).get(id)
   
   if orga == None:
       flash('ID no encontrado')
       return redirect(url_for('Organizadores'))
   
   image_paths = [orga.Imagen, orga.IMG2]
    
   base_path = 'static/imagenes/Griferia/Organizadores'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(orga)
   db_session.commit()
   
   return redirect(url_for('Organizadores'))  

#---------------- Asientos --------------
@app.post('/Add_Asiento')
def Add_Asiento():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Tip = request.form['Tipo']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Asiento'], new_filename))
                return os.path.join(app.config['IMGS_GF_Asiento'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_asiento = models.Asiento(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Tipo =Tip,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_asiento)
    db_session.commit()
    return redirect("Asientos")

@app.post('/Act_Asiento/<id>')
def Act_Asiento(id):
    asiento_act = db_session.query(models.Asiento).get(id)
       
    if asiento_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Asientos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Tip_act = request.form['Tipo_act']
    
    if asiento_act == None:
        flash('No hay nada')
        return redirect (url_for('Asientos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Asiento'], new_filename))
                return os.path.join(app.config['IMGS_GF_Asiento'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    asiento_act.Imagen = update_image('Imagen_act', asiento_act.Imagen)
    asiento_act.IMG2 = update_image('IMG2_act', asiento_act.IMG2)
       
    asiento_act.Nombre = Name_act
    asiento_act.Precio = Prec_act
    asiento_act.Codigo = Cod_act
    asiento_act.Marca = Marc_act
    asiento_act.Color = Col_act
    asiento_act.Medida = Med_act
    asiento_act.Tipo = Tip_act

    db_session.add(asiento_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Asientos'))

@app.get('/E_Asiento/<id>')
def E_Asiento(id):
   asiento = db_session.query(models.Asiento).get(id)
   
   if asiento == None:
       flash('ID no encontrado')
       return redirect(url_for('Asientos'))
   
   image_paths = [asiento.Imagen, asiento.IMG2]
    
   base_path = 'static/imagenes/Griferia/Asientos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(asiento)
   db_session.commit()
   
   return redirect(url_for('Asientos'))  

#---------------- Ovalines --------------
@app.post('/Add_Ovalin')
def Add_Ovalin():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Tip = request.form['Tipo_colocacion']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Ovalin'], new_filename))
                return os.path.join(app.config['IMGS_GF_Ovalin'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_ovalin = models.Ovalin(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Tipo_colocacion =Tip,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_ovalin)
    db_session.commit()
    return redirect("Ovalines")

@app.post('/Act_Ovalin/<id>')
def Act_Ovalin(id):
    ovalin_act = db_session.query(models.Ovalin).get(id)
       
    if ovalin_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Ovalines'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Tip_act = request.form['Tipo_colocacion_act']
    
    if ovalin_act == None:
        flash('No hay nada')
        return redirect (url_for('Ovalines'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Ovalin'], new_filename))
                return os.path.join(app.config['IMGS_GF_Ovalin'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    ovalin_act.Imagen = update_image('Imagen_act', ovalin_act.Imagen)
    ovalin_act.IMG2 = update_image('IMG2_act', ovalin_act.IMG2)
       
    ovalin_act.Nombre = Name_act
    ovalin_act.Precio = Prec_act
    ovalin_act.Codigo = Cod_act
    ovalin_act.Marca = Marc_act
    ovalin_act.Color = Col_act
    ovalin_act.Medida = Med_act
    ovalin_act.Material = Mat_act
    ovalin_act.Tipo_colocacion = Tip_act

    db_session.add(ovalin_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Ovalines'))

@app.get('/E_Ovalin/<id>')
def E_Ovalin(id):
   ovalin = db_session.query(models.Ovalin).get(id)
   if ovalin == None:
       flash('ID no encontrado')
       return redirect(url_for('Ovalines'))
   
   image_paths = [ovalin.Imagen, ovalin.IMG2]
    
   base_path = 'static/imagenes/Griferia/Ovalines'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(ovalin)
   db_session.commit()
   return redirect(url_for('Ovalines'))  

#---------------- Separadores --------------
@app.post('/Add_Separador')
def Add_Separador():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Separador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Separador'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_separador = models.Separador(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_separador)
    db_session.commit()
    return redirect("Separadores")

@app.post('/Act_Separador/<id>')
def Act_Separador(id):
    separador_act = db_session.query(models.Separador).get(id)
       
    if separador_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Separadores'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
      
    if separador_act == None:
        flash('No hay nada')
        return redirect (url_for('Separadores'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Separador'], new_filename))
                return os.path.join(app.config['IMGS_GF_Separador'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    separador_act.Imagen = update_image('Imagen_act', separador_act.Imagen)
    separador_act.IMG2 = update_image('IMG2_act', separador_act.IMG2)
       
    separador_act.Nombre = Name_act
    separador_act.Precio = Prec_act
    separador_act.Codigo = Cod_act
    separador_act.Marca = Marc_act
    separador_act.Color = Col_act
    separador_act.Medida = Med_act
    separador_act.Material = Mat_act

    db_session.add(separador_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Separadores'))

@app.get('/E_Separador/<id>')
def E_Separador(id):
   sepa = db_session.query(models.Separador).get(id)
   
   if sepa == None:
       flash('ID no encontrado')
       return redirect(url_for('Separadores'))
   
   image_paths = [sepa.Imagen, sepa.IMG2]
    
   base_path = 'static/imagenes/Griferia/Separadores'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(sepa)
   db_session.commit()
   
   return redirect(url_for('Separadores')) 

#---------------- Herramientas --------------
@app.post('/Add_Herramienta')
def Add_Herramienta():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_HerramientaCol'], new_filename))
                return os.path.join(app.config['IMGS_GF_HerramientaCol'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_herra = models.Herramienta_Col(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_herra)
    db_session.commit()
    return redirect("Herramientas")

@app.post('/Act_Herramienta/<id>')
def Act_Herramienta(id):
    herra_act = db_session.query(models.Herramienta_Col).get(id)
       
    if herra_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Herramientas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']

    if herra_act == None:
        flash('No hay nada')
        return redirect (url_for('Herramientas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_HerramientaCol'], new_filename))
                return os.path.join(app.config['IMGS_GF_HerramientaCol'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    herra_act.Imagen = update_image('Imagen_act', herra_act.Imagen)
    herra_act.IMG2 = update_image('IMG2_act', herra_act.IMG2)
       
    herra_act.Nombre = Name_act
    herra_act.Precio = Prec_act
    herra_act.Codigo = Cod_act
    herra_act.Marca = Marc_act
    herra_act.Medida = Med_act
    herra_act.Material = Mat_act

    db_session.add(herra_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Herramientas'))

@app.get('/E_Herramienta/<id>')
def E_Herramienta(id):
   herr = db_session.query(models.Herramienta_Col).get(id)
   
   if herr == None:
       flash('ID no encontrado')
       return redirect(url_for('Herramientas'))
   
   image_paths = [herr.Imagen, herr.IMG2]
    
   base_path = 'static/imagenes/Griferia/Herramientas_Col'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(herr)
   db_session.commit()
   
   return redirect(url_for('Herramientas'))  

#---------------- Calentadores Solares --------------
@app.post('/Add_CalentadorS')
def Add_CalentadorS():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cap = request.form['Capacidad']
    Com = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_CalentadorS'], new_filename))
                return os.path.join(app.config['IMGS_GF_CalentadorS'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_calentador = models.Calentador_S(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        color = Col,
        Marca =Marc,
        Material =Mat,
        Capacidad = Cap,
        Complementos = Com,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_calentador)
    db_session.commit()
    return redirect("CalentadoresS")

@app.post('/Act_CalentadorS/<id>')
def Act_CalentadorS(id):
    calentador_act = db_session.query(models.Calentador_S).get(id)
       
    if calentador_act == None:
        flash('ID no encontrado')
        return redirect (url_for('CalentadoresS'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Col_act = request.form['Color_act']
    Marc_act = request.form['Marca_act']
    Mat_act = request.form['Material_act']
    Cap_act = request.form['Capacidad_act']
    Com_act = request.form['Complementos_act']
      
    if calentador_act == None:
        flash('No hay nada')
        return redirect (url_for('CalentadoresS'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_CalentadorS'], new_filename))
                return os.path.join(app.config['IMGS_GF_CalentadorS'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    calentador_act.Imagen = update_image('Imagen_act', calentador_act.Imagen)
    calentador_act.IMG2 = update_image('IMG2_act', calentador_act.IMG2)
       
    calentador_act.Nombre = Name_act
    calentador_act.Precio = Prec_act
    calentador_act.Codigo = Cod_act
    calentador_act.color = Col_act
    calentador_act.Marca = Marc_act
    calentador_act.Material = Mat_act
    calentador_act.Capacidad = Cap_act
    calentador_act.Complementos = Com_act

    db_session.add(calentador_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('CalentadoresS'))

@app.get('/E_CalentadorS/<id>')
def E_CalentadorS(id):
   CalentadorS = db_session.query(models.Calentador_S).get(id)
   
   if CalentadorS == None:
       flash('ID no encontrado')
       return redirect(url_for('CalentadoresS'))
   
   image_paths = [CalentadorS.Imagen, CalentadorS.IMG2]
    
   base_path = 'static/imagenes/Griferia/Calentadores_S'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(CalentadorS)
   db_session.commit()
   
   return redirect(url_for('CalentadoresS'))  

#---------------- Calentadores de Paso --------------
@app.post('/Add_CalentadorP')
def Add_CalentadorP():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cap = request.form['Capacidad']
    Serv = request.form['Servicio']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_CalentadorP'], new_filename))
                return os.path.join(app.config['IMGS_GF_CalentadorP'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_calentadorp = models.Calentador_P(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        color = Col,
        Marca =Marc,
        Material =Mat,
        Capacidad = Cap,
        Servicios = Serv,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_calentadorp)
    db_session.commit()
    return redirect("CalentadoresP")

@app.post('/Act_CalentadorP/<id>')
def Act_CalentadorP(id):
    calentadorp_act = db_session.query(models.Calentador_P).get(id)
       
    if calentadorp_act == None:
        flash('ID no encontrado')
        return redirect (url_for('CalentadoresP'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Col_act = request.form['Color_act']
    Marc_act = request.form['Marca_act']
    Mat_act = request.form['Material_act']
    Cap_act = request.form['Capacidad_act']
    Serv_act = request.form['Servicio_act']
       
    if calentadorp_act == None:
        flash('No hay nada')
        return redirect (url_for('CalentadoresP'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_CalentadorP'], new_filename))
                return os.path.join(app.config['IMGS_GF_CalentadorP'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    calentadorp_act.Imagen = update_image('Imagen_act', calentadorp_act.Imagen)
    calentadorp_act.IMG2 = update_image('IMG2_act', calentadorp_act.IMG2)
       
    calentadorp_act.Nombre = Name_act
    calentadorp_act.Precio = Prec_act
    calentadorp_act.Codigo = Cod_act
    calentadorp_act.color = Col_act
    calentadorp_act.Marca = Marc_act
    calentadorp_act.Material = Mat_act
    calentadorp_act.Capacidad = Cap_act
    calentadorp_act.Servicios = Serv_act
   
    db_session.add(calentadorp_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('CalentadoresP'))

@app.get('/E_CalentadorP/<id>')
def E_CalentadorP(id):
   CalentadorP = db_session.query(models.Calentador_P).get(id)
   
   if CalentadorP == None:
       flash('ID no encontrado')
       return redirect(url_for('CalentadoresP'))
   
   image_paths = [CalentadorP.Imagen, CalentadorP.IMG2]
    
   base_path = 'static/imagenes/Griferia/Calentadores_P'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(CalentadorP)
   db_session.commit()
   
   return redirect(url_for('CalentadoresP'))

#---------------- Espejos --------------
@app.post('/Add_Espejo')
def Add_Espejo():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Mat = request.form['Material']
    Com = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Espejo'], new_filename))
                return os.path.join(app.config['IMGS_GF_Espejo'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_espejo = models.Espejo(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        color = Col,
        Complementos =Com,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_espejo)
    db_session.commit()
    return redirect("Espejos")

@app.post('/Act_Espejo/<id>')
def Act_Espejo(id):
    espejo_act = db_session.query(models.Espejo).get(id)
       
    if espejo_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Espejos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Med_act = request.form['Medida_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']
    Com_act = request.form['Complementos_act']  
       
    if espejo_act == None:
        flash('No hay nada')
        return redirect (url_for('Espejos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Espejo'], new_filename))
                return os.path.join(app.config['IMGS_GF_Espejo'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    espejo_act.Imagen = update_image('Imagen_act', espejo_act.Imagen)
    espejo_act.IMG2 = update_image('IMG2_act', espejo_act.IMG2)
       
    espejo_act.Nombre = Name_act
    espejo_act.Precio = Prec_act
    espejo_act.Codigo = Cod_act
    espejo_act.Medida = Med_act
    espejo_act.color = Col_act
    espejo_act.Material = Mat_act
    espejo_act.Complementos = Com_act

    db_session.add(espejo_act)
    db_session.commit()
    flash('Actualización exitosa')    
    return redirect(url_for('Espejos'))

@app.get('/E_Espejo/<id>')
def E_Espejo(id):
   espejo = db_session.query(models.Espejo).get(id)
   
   if espejo == None:
       flash('ID no encontrado')
       return redirect(url_for('Espejos'))
   
   image_paths = [espejo.Imagen, espejo.IMG2]
    
   base_path = 'static/imagenes/Griferia/Espejos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(espejo)
   db_session.commit()
   
   return redirect(url_for('Espejos')) 

#---------------- Repisas --------------
@app.post('/Add_Repisa')
def Add_Repisa():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Repisa'], new_filename))
                return os.path.join(app.config['IMGS_GF_Repisa'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_repisa = models.Repisa(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca = Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_repisa)
    db_session.commit()
    return redirect("Repisas")

@app.post('/Act_Repisa/<id>')
def Act_Repisa(id):
    repisa_act = db_session.query(models.Repisa).get(id)
       
    if repisa_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Repisas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Med_act = request.form['Medida_act']
    Col_act = request.form['Color_act']
    Marc_act = request.form['Marca_act']
    Mat_act = request.form['Material_act']
       
    if repisa_act == None:
        flash('No hay nada')
        return redirect (url_for('Repisas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Repisa'], new_filename))
                return os.path.join(app.config['IMGS_GF_Repisa'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    repisa_act.Imagen = update_image('Imagen_act', repisa_act.Imagen)
    repisa_act.IMG2 = update_image('IMG2_act', repisa_act.IMG2)
       
    repisa_act.Nombre = Name_act
    repisa_act.Precio = Prec_act
    repisa_act.Codigo = Cod_act
    repisa_act.Medida = Med_act
    repisa_act.Color = Col_act
    repisa_act.Marca = Marc_act
    repisa_act.Material = Mat_act
 
    db_session.add(repisa_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Repisas'))

@app.get('/E_Repisa/<id>')
def E_Repisa(id):
   repisa = db_session.query(models.Repisa).get(id)
   
   if repisa == None:
       flash('ID no encontrado')
       return redirect(url_for('Repisas'))
   
   image_paths = [repisa.Imagen, repisa.IMG2]
    
   base_path = 'static/imagenes/Griferia/Repisas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(repisa)
   db_session.commit()
   
   return redirect(url_for('Repisas')) 

#---------------- Resumideros --------------
@app.post('/Add_Resumidero')
def Add_Resumidero():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Resumidero'], new_filename))
                return os.path.join(app.config['IMGS_GF_Resumidero'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_resumidero = models.Resumidero(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_resumidero)
    db_session.commit()
    return redirect("Resumideros")

@app.post('/Act_Resumidero/<id>')
def Act_Resumidero(id):
    resu_act = db_session.query(models.Resumidero).get(id)
       
    if resu_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Resumideros'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Med_act = request.form['Medida_act']
    Col_act = request.form['Color_act']
    Mat_act = request.form['Material_act']   
       
    if resu_act == None:
        flash('No hay nada')
        return redirect (url_for('Resumideros'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Resumidero'], new_filename))
                return os.path.join(app.config['IMGS_GF_Resumidero'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    resu_act.Imagen = update_image('Imagen_act', resu_act.Imagen)
    resu_act.IMG2 = update_image('IMG2_act', resu_act.IMG2)
       
    resu_act.Nombre = Name_act
    resu_act.Precio = Prec_act
    resu_act.Codigo = Cod_act
    resu_act.Medida = Med_act
    resu_act.Color = Col_act
    resu_act.Material = Mat_act

    db_session.add(resu_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Resumideros'))

@app.get('/E_Resumidero/<id>')
def E_Resumidero(id):
   resumi = db_session.query(models.Resumidero).get(id)
   
   if resumi == None:
       flash('ID no encontrado')
       return redirect(url_for('Resumideros'))
   
   image_paths = [resumi.Imagen, resumi.IMG2]
    
   base_path = 'static/imagenes/Griferia/Resumideros'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(resumi)
   db_session.commit()
   
   return redirect(url_for('Resumideros')) 

#---------------- Contra canastas --------------
@app.post('/Add_Contracanasta')
def Add_Contracanasta():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_ContraC'], new_filename))
                return os.path.join(app.config['IMGS_GF_ContraC'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_contraC = models.Contra_Can(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_contraC)
    db_session.commit()
    return redirect("Contracanastas")

@app.post('/Act_Contracanasta/<id>')
def Act_Contracanasta(id):
    contra_act = db_session.query(models.Contra_Can).get(id)
       
    if contra_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Contracanastas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
     
    if contra_act == None:
        flash('No hay nada')
        return redirect (url_for('Contracanastas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_ContraC'], new_filename))
                return os.path.join(app.config['IMGS_GF_ContraC'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    contra_act.Imagen = update_image('Imagen_act',contra_act.Imagen)
    contra_act.IMG2 = update_image('IMG2_act',contra_act.IMG2)
       
    contra_act.Nombre = Name_act
    contra_act.Precio = Prec_act
    contra_act.Codigo = Cod_act
    contra_act.Marca = Marc_act
    contra_act.Color = Col_act
    contra_act.Medida = Med_act
    contra_act.Material = Mat_act

    db_session.add(contra_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Contracanastas'))

@app.get('/E_Contracanasta/<id>')
def E_Contracanasta(id):
   contra = db_session.query(models.Contra_Can).get(id)
   
   if contra == None:
       flash('ID no encontrado')
       return redirect(url_for('Contracanastas'))
   
   image_paths = [contra.Imagen, contra.IMG2]
    
   base_path = 'static/imagenes/Griferia/Contracanastas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(contra)
   db_session.commit()
   
   return redirect(url_for('Contracanastas')) 

#---------------- Cespol --------------
@app.post('/Add_Cespol')
def Add_Cespol():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Cespol'], new_filename))
                return os.path.join(app.config['IMGS_GF_Cespol'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_cespol = models.Cespol(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_cespol)
    db_session.commit()
    return redirect("Cespols")

@app.post('/Act_Cespol/<id>')
def Act_Cespol(id):
    cespol_act = db_session.query(models.Cespol).get(id)
       
    if cespol_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Cespols'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    
    if cespol_act == None:
        flash('No hay nada')
        return redirect (url_for('Cespols'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Cespol'], new_filename))
                return os.path.join(app.config['IMGS_GF_Cespol'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    cespol_act.Imagen = update_image('Imagen_act', cespol_act.Imagen)
    cespol_act.IMG2 = update_image('IMG2_act', cespol_act.IMG2)
       
    cespol_act.Nombre = Name_act
    cespol_act.Precio = Prec_act
    cespol_act.Codigo = Cod_act
    cespol_act.Marca = Marc_act
    cespol_act.Color = Col_act
    cespol_act.Medida = Med_act
    cespol_act.Material = Mat_act

    db_session.add(cespol_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Cespols'))

@app.get('/E_Cespol/<id>')
def E_Cespol(id):
   cespol = db_session.query(models.Cespol).get(id)
   
   if cespol == None:
       flash('ID no encontrado')
       return redirect(url_for('Cespols'))
   
   image_paths = [cespol.Imagen, cespol.IMG2]
    
   base_path = 'static/imagenes/Griferia/Cespols'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(cespol)
   db_session.commit()
   
   return redirect(url_for('Cespols')) 

#---------------- Impermeabilizantes --------------
@app.post('/Add_Imper')
def Add_Imper():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Cont = request.form['Contenido']
    Dur = request.form['Duracion']
    Car = request.form['Caracteristicas']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Impermeabilizante'], new_filename))
                return os.path.join(app.config['IMGS_GF_Impermeabilizante'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_imper = models.Impermeabilizante(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Color = Col,
        Marca =Marc,
        Contenido =Cont,
        Duracion = Dur,
        Caracteristicas = Car,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_imper)
    db_session.commit()
    return redirect("Impers")

@app.post('/Act_Imper/<id>')
def Act_Imper(id):
    imper_act = db_session.query(models.Impermeabilizante).get(id)
       
    if imper_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Impers'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Cont_act = request.form['Contenido_act']
    Dur_act = request.form['Duracion_act']
    Car_act = request.form['Caracteristicas_act']
 
    if imper_act == None:
        flash('No hay nada')
        return redirect (url_for('Impers'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Impermeabilizante'], new_filename))
                return os.path.join(app.config['IMGS_GF_Impermeabilizante'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    imper_act.Imagen = update_image('Imagen_act', imper_act.Imagen)
    imper_act.IMG2 = update_image('IMG2_act', imper_act.IMG2)
       
    imper_act.Nombre = Name_act
    imper_act.Precio = Prec_act
    imper_act.Codigo = Cod_act
    imper_act.Marca = Marc_act
    imper_act.Color = Col_act
    imper_act.Contenido = Cont_act
    imper_act.Duracion = Dur_act
    imper_act.Caracteristicas = Car_act

    db_session.add(imper_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Impers'))

@app.get('/E_Imper/<id>')
def E_Imper(id):
   imper = db_session.query(models.Impermeabilizante).get(id)
   
   if imper == None:
       flash('ID no encontrado')
       return redirect(url_for('Impers'))
   
   image_paths = [imper.Imagen, imper.IMG2]
    
   base_path = 'static/imagenes/Griferia/Impermeabilizantes'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(imper)
   db_session.commit()
   
   return redirect(url_for('Impers')) 

#---------------- Paneles y Canceles --------------
@app.post('/Add_Panel')
def Add_Panel():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Com = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_PanelCancel'], new_filename))
                return os.path.join(app.config['IMGS_GF_PanelCancel'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_panel = models.Panel_Cancel(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Complementos =Com,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_panel)
    db_session.commit()
    return redirect("Paneles")

@app.post('/Act_Panel/<id>')
def Act_Panel(id):
    panel_act = db_session.query(models.Panel_Cancel).get(id)
       
    if panel_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Paneles'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Com_act = request.form['Complementos_act']

    if panel_act == None:
        flash('No hay nada')
        return redirect (url_for('Paneles'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_PanelCancel'], new_filename))
                return os.path.join(app.config['IMGS_GF_PanelCancel'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    panel_act.Imagen = update_image('Imagen_act', panel_act.Imagen)
    panel_act.IMG2 = update_image('IMG2_act', panel_act.IMG2)
       
    panel_act.Nombre = Name_act
    panel_act.Precio = Prec_act
    panel_act.Codigo = Cod_act
    panel_act.Marca = Marc_act
    panel_act.Color = Col_act
    panel_act.Medida = Med_act
    panel_act.Material = Mat_act
    panel_act.Complementos = Com_act
 
    db_session.add(panel_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Paneles'))

@app.get('/E_Panel/<id>')
def E_Panel(id):
   panel = db_session.query(models.Panel_Cancel).get(id)
   
   if panel == None:
       flash('ID no encontrado')
       return redirect(url_for('Paneles'))
   
   image_paths = [panel.Imagen, panel.IMG2]
    
   base_path = 'static/imagenes/Griferia/Panel_Canceles'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(panel)
   db_session.commit()
   
   return redirect(url_for('Paneles'))  

#---------------- Tinas --------------
@app.post('/Add_Tina')
def Add_Tina():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cap = request.form['Capacidad']
    Tip = request.form['Tipo']
    Com = request.form['Complementos']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_GF_Tina'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tina'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nueva_tina = models.Tina(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Capacidad =Cap,
        Tipo =Tip,
        Complementos =Com,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nueva_tina)
    db_session.commit()
    return redirect("Tinas")

@app.post('/Act_Tina/<id>')
def Act_Tina(id):
    tina_act = db_session.query(models.Tina).get(id)
       
    if tina_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tinas'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Cap_act = request.form['Capacidad_act']
    Tip_act = request.form['Tipo_act']
    Com_act = request.form['Complementos_act']
   
    if tina_act == None:
        flash('No hay nada')
        return redirect (url_for('Tinas'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_GF_Tina'], new_filename))
                return os.path.join(app.config['IMGS_GF_Tina'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    tina_act.Imagen = update_image('Imagen_act', tina_act.Imagen)
    tina_act.IMG2 = update_image('IMG2_act', tina_act.IMG2)
       
    tina_act.Nombre = Name_act
    tina_act.Precio = Prec_act
    tina_act.Codigo = Cod_act
    tina_act.Marca = Marc_act
    tina_act.Color = Col_act
    tina_act.Medida = Med_act
    tina_act.Material = Mat_act
    tina_act.Capacidad = Cap_act
    tina_act.Tipo = Tip_act
    tina_act.Complementos = Com_act

    db_session.add(tina_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Tinas'))

@app.get('/E_Tina/<id>')
def E_Tina(id):
   tina = db_session.query(models.Tina).get(id)
   
   if tina == None:
       flash('ID no encontrado')
       return redirect(url_for('Tinas'))
   
   image_paths = [tina.Imagen, tina.IMG2]
    
   base_path = 'static/imagenes/Griferia/Tinas'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(tina)
   db_session.commit()
   
   return redirect(url_for('Tinas'))  

# --------------------------------------- Registro de productos Baños -----------------------------------------
#---------------- Inodoros --------------
@app.post('/Add_Inodoro')
def Add_Inodoro():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Mod = request.form['Modelo']
    Cal = request.form['Calidad']
    Con = request.form['Consumo_agua']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_BN_Inodoro'], new_filename))
                return os.path.join(app.config['IMGS_BN_Inodoro'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_inodoro = models.Inodoro(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Modelo =Mod,
        Calidad =Cal,
        Consumo_agua =Con,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_inodoro)
    db_session.commit()
    return redirect("Inodoros")

@app.post('/Act_Inodoro/<id>')
def Act_Inodoro(id):
    inod_act = db_session.query(models.Inodoro).get(id)
       
    if inod_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Inodoros'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Mod_act = request.form['PrecioAnt_act']
    Cal_act = request.form['Calidad_act']
    Con_act = request.form['Consumo_agua_act']
     
    if inod_act == None:
        flash('No hay nada')
        return redirect (url_for('Inodoros'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_BN_Inodoro'], new_filename))
                return os.path.join(app.config['IMGS_BN_Inodoro'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    inod_act.Imagen = update_image('Imagen_act', inod_act.Imagen)
    inod_act.IMG2 = update_image('IMG2_act', inod_act.IMG2)
       
    inod_act.Nombre = Name_act
    inod_act.Precio = Prec_act
    inod_act.Codigo = Cod_act
    inod_act.Marca = Marc_act
    inod_act.Color = Col_act
    inod_act.Medida = Med_act
    inod_act.Material = Mat_act
    inod_act.PrecioAnt = Mod_act
    inod_act.Calidad = Cal_act
    inod_act.Consumo_agua = Con_act

    db_session.add(inod_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Inodoros'))

@app.get('/E_Inodoro/<id>')
def E_Inodoro(id):
   inod = db_session.query(models.Inodoro).get(id)
   
   if inod == None:
       flash('ID no encontrado')
       return redirect(url_for('Inodoros'))
   
   image_paths = [inod.Imagen, inod.IMG2]
   base_path = 'static/imagenes/Banos/Inodoros/'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(inod)
   db_session.commit()
   
   return redirect(url_for('Inodoros'))

#---------------- Migitorio --------------
@app.post('/Add_Migitorio')
def Add_Migitorio():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Aca = request.form['Acabado']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_BN_Migitorio'], new_filename))
                return os.path.join(app.config['IMGS_BN_Migitorio'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_mig = models.Migitorio(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Acabado =Aca,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_mig)
    db_session.commit()
    return redirect("Migitorios")

@app.post('/Act_Migitorio/<id>')
def Act_Migitorio(id):
    migi_act = db_session.query(models.Migitorio).get(id)
       
    if migi_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Migitorios'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Aca_act = request.form['Acabado_act']

    if migi_act == None:
        flash('No hay nada')
        return redirect (url_for('Migitorios'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_BN_Migitorio'], new_filename))
                return os.path.join(app.config['IMGS_BN_Migitorio'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    migi_act.Imagen = update_image('Imagen_act', migi_act.Imagen)
    migi_act.IMG2 = update_image('IMG2_act', migi_act.IMG2)
       
    migi_act.Nombre = Name_act
    migi_act.Precio = Prec_act
    migi_act.Codigo = Cod_act
    migi_act.Marca = Marc_act
    migi_act.Color = Col_act
    migi_act.Medida = Med_act
    migi_act.Material = Mat_act
    migi_act.Acabado = Aca_act

    db_session.add(migi_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Migitorios'))

@app.get('/E_Migitorio/<id>')
def E_Migitorio(id):
   migi = db_session.query(models.Migitorio).get(id)
   
   if migi == None:
       flash('ID no encontrado')
       return redirect(url_for('Migitorios'))
   
   image_paths = [migi.Imagen, migi.IMG2]
    
   base_path = 'static/imagenes/Banos/Migitorios'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(migi)
   db_session.commit()
   
   return redirect(url_for('Migitorios'))  

#---------------- Lavabos --------------
@app.post('/Add_Lavabo')
def Add_Lavabo():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_BN_Lavabo'], new_filename))
                return os.path.join(app.config['IMGS_BN_Lavabo'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_lav = models.Lavabo(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_lav)
    db_session.commit()
    return redirect("Lavabos")

@app.post('/Act_Lavabo/<id>')
def Act_Lavabo(id):
    lava_act = db_session.query(models.Lavabo).get(id)
       
    if lava_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Lavabos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']

    if lava_act == None:
        flash('No hay nada')
        return redirect (url_for('Lavabos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_BN_Lavabo'], new_filename))
                return os.path.join(app.config['IMGS_BN_Lavabo'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    lava_act.Imagen = update_image('Imagen_act', lava_act.Imagen)
    lava_act.IMG2 = update_image('IMG2_act', lava_act.IMG2)
       
    lava_act.Nombre = Name_act
    lava_act.Precio = Prec_act
    lava_act.Codigo = Cod_act
    lava_act.Marca = Marc_act
    lava_act.Color = Col_act
    lava_act.Medida = Med_act
    lava_act.Material = Mat_act

    db_session.add(lava_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Lavabos'))

@app.get('/E_Lavabo/<id>')
def E_Lavabo(id):
   lava = db_session.query(models.Lavabo).get(id)
   
   if lava == None:
       flash('ID no encontrado')
       return redirect(url_for('Lavabos'))
   
   image_paths = [lava.Imagen, lava.IMG2]
    
   base_path = 'static/imagenes/Banos/Lavabos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(lava)
   db_session.commit()
   
   return redirect(url_for('Lavabos'))  

#---------------- Kit Sanitarios --------------
@app.post('/Add_Kit_san')
def Add_Kit_san():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cal = request.form['Calidad']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_BN_KitSanitario'], new_filename))
                return os.path.join(app.config['IMGS_BN_KitSanitario'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_kisan = models.Kit_Sanitario(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Calidad =Cal,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_kisan)
    db_session.commit()
    return redirect("Kit_sans")

@app.post('/Act_Kit_san/<id>')
def Act_Kit_san(id):
    kisan_act = db_session.query(models.Kit_Sanitario).get(id)
       
    if kisan_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Kit_sans'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Cal_act = request.form['Calidad_act']
    
    if kisan_act == None:
        flash('No hay nada')
        return redirect (url_for('Kit_sans'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_BN_KitSanitario'], new_filename))
                return os.path.join(app.config['IMGS_BN_KitSanitario'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    kisan_act.Imagen = update_image('Imagen_act', kisan_act.Imagen)
    kisan_act.IMG2 = update_image('IMG2_act', kisan_act.IMG2)
       
    kisan_act.Nombre = Name_act
    kisan_act.Precio = Prec_act
    kisan_act.Codigo = Cod_act
    kisan_act.Marca = Marc_act
    kisan_act.Color = Col_act
    kisan_act.Medida = Med_act
    kisan_act.Material = Mat_act
    kisan_act.Calidad = Cal_act

    db_session.add(kisan_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Kit_sans'))

@app.get('/E_Kit_san/<id>')
def E_Kit_san(id):
   kisa = db_session.query(models.Kit_Sanitario).get(id)
   
   if kisa == None:
       flash('ID no encontrado')
       return redirect(url_for('Kit_sans'))
   
   image_paths = [kisa.Imagen, kisa.IMG2]
    
   base_path = 'static/imagenes/Banos/Kit_Sanitarios'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(kisa)
   db_session.commit()
   
   return redirect(url_for('Kit_sans'))  

#---------------- Tinacos --------------
@app.post('/Add_Tinaco')
def Add_Tinaco():
    Name = request.form['Nombre']
    Pre = request.form['Precio']
    PreAnt = request.form['PrecioAnt']
    Cod= request.form['Codigo']
    Med = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Cal = request.form['Calidad']
    Cap = request.form['Capacidad']

    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_BN_Tinaco'], new_filename))
                return os.path.join(app.config['IMGS_BN_Tinaco'], new_filename)
        return None

    Imag = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_tinaco = models.Tinacos(
        Nombre = Name,
        Precio = Pre,
        PrecioAnt = PreAnt,
        Codigo= Cod,
        Medida = Med,
        Color = Col,
        Marca =Marc,
        Material =Mat,
        Calidad =Cal,
        Capacidad =Cap,
        Imagen = Imag,
        IMG2 = Img2,
    )
    db_session.add(nuevo_tinaco)
    db_session.commit()
    return redirect("Tinacos")

@app.post('/Act_Tinaco/<id>')
def Act_Tinaco(id):
    tinaco_act = db_session.query(models.Tinacos).get(id)
       
    if tinaco_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Tinacos'))
       
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Mat_act = request.form['Material_act']
    Cal_act = request.form['Calidad_act']
    Cap_act = request.form['Capacidad_act']

    if tinaco_act == None:
        flash('No hay nada')
        return redirect (url_for('Tinacos'))
    
    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_BN_Tinaco'], new_filename))
                return os.path.join(app.config['IMGS_BN_Tinaco'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    tinaco_act.Imagen = update_image('Imagen_act', tinaco_act.Imagen)
    tinaco_act.IMG2 = update_image('IMG2_act', tinaco_act.IMG2)
       
    tinaco_act.Nombre = Name_act
    tinaco_act.Precio = Prec_act
    tinaco_act.Codigo = Cod_act
    tinaco_act.Marca = Marc_act
    tinaco_act.Color = Col_act
    tinaco_act.Medida = Med_act
    tinaco_act.Material = Mat_act
    tinaco_act.Calidad = Cal_act
    tinaco_act.Capacidad = Cap_act

    db_session.add(tinaco_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Tinacos'))

@app.get('/E_Tinaco/<id>')
def E_Tinaco(id):
   tinac = db_session.query(models.Tinacos).get(id)
   
   if tinac == None:
       flash('ID no encontrado')
       return redirect(url_for('Tinacos'))
   
   image_paths = [tinac.Imagen, tinac.IMG2]
    
   base_path = 'static/imagenes/Banos/Tinacos'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(tinac)
   db_session.commit()
   
   return redirect(url_for('Tinacos'))

#---------------------------------------- Seccion de Ofertas ---------------------------------------------

@app.post('/regPisos_Mur')
def regPisos_Mur():
    Nom = request.form['Nombre']
    Cod = request.form['Codigo']
    Prec = request.form['Precio']
    Prec_ant = request.form['Precio_anterior']
    Medi = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_OFF_PisMur'], new_filename))
                return os.path.join(app.config['IMGS_OFF_PisMur'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_product = models.Pisos_Mur(
        Nombre = Nom,
        Codigo = Cod,
        Precio = Prec, 
        Precio_ant = Prec_ant,
        Medida = Medi,
        Color = Col,
        Marca = Marc,
        Material = Mat,
        Acabado = Acab,
        Contenido = Cont,
        Calidad = Cal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nuevo_product)
    db_session.commit()
    return redirect("OFF_PM")



@app.post('/Act_Pisos_Mur/<id>')
def Act_Pisos_Mur(id):
    producto_act = db_session.query(models.Pisos_Mur).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('OFF_PM'))
       
    Name_act = request.form['Nombre_act']
    Cod_act = request.form['Codigo_act']
    Prec_act = request.form['Precio_act']
    Prec_ant_act = request.form['Precio_anterior_act']
    Med_act = request.form['Medida_act']
    Col_act = request.form['Color_act']
    Marc_act = request.form['Marca_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('OFF_PM'))

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_OFF_PisMur'], new_filename))
                return os.path.join(app.config['IMGS_OFF_PisMur'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Precio_ant = Prec_ant_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido=Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('OFF_PM'))

@app.get('/E_Pisos_Mur/<id>')
def E_Pisos_Mur(id):
   product = db_session.query(models.Pisos_Mur).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('OFF_PM'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Ofertas/PM'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('OFF_PM'))


@app.post('/regGrif_Ban')
def regGrif_Ban():
    Nom = request.form['Nombre']
    Cod = request.form['Codigo']
    Prec = request.form['Precio']
    Prec_ant = request.form['Precio_anterior']
    Medi = request.form['Medida']
    Col = request.form['Color']
    Marc = request.form['Marca']
    Mat = request.form['Material']
    Detal = request.form['Detalles']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_OFF_GrifBan'], new_filename)) 
                return os.path.join(app.config['IMGS_OFF_GrifBan'], new_filename) 
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    
    nuevo_product = models.Grif_Ban(
        Nombre = Nom,
        Codigo = Cod,
        Precio = Prec, 
        Precio_ant = Prec_ant,
        Medida = Medi,
        Color = Col,
        Marca = Marc,
        Material = Mat,
        Detalles = Detal,
        Imagen = Img,
        IMG2 = Img2,
        
    )
    db_session.add(nuevo_product)
    db_session.commit()
    return redirect("OFF_GB")

@app.post('/Act_Grif_Ban/<id>')
def Act_Grif_Ban(id):
    producto_act = db_session.query(models.Grif_Ban).get(id)
       
    if producto_act == None:
        flash('ID no encontrado')
        return redirect (url_for('OFF_GB'))
       
    Name_act = request.form['Nombre_act']
    Cod_act = request.form['Codigo_act']
    Prec_act = request.form['Precio_act']
    Prec_ant_act = request.form['Precio_anterior_act']
    Med_act = request.form['Medida_act']
    Col_act = request.form['Color_act']
    Marc_act = request.form['Marca_act']
    Mat_act = request.form['Material_act']
    Detal_act = request.form['Detalles_act']
    
    
    if producto_act == None:
        flash('No hay nada')
        return redirect (url_for('OFF_GB'))

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{unique_id}_{name}{ext}" 
            try:
                file.save(os.path.join(app.config['IMGS_OFF_GrifBan'], new_filename))
                return os.path.join(app.config['IMGS_OFF_GrifBan'], new_filename) 
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None
        else:
            return None
    
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path) 
        return new_image_path if new_image_path else current_image_path

    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)
       
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Precio_ant = Prec_ant_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.Material = Mat_act
    producto_act.Detalles = Detal_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('OFF_GB'))

@app.get('/E_Grif_Ban/<id>')
def E_Grif_Ban(id):
   product = db_session.query(models.Grif_Ban).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('OFF_GB'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Ofertas/GB'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('OFF_GB'))

#------------------------------------------------ Lo más vendido -------------------------------------------------
# Rutas para el registro de productos en pisos de vitro
@app.post('/regVitro_Masvend')
def regVitro_Masvend():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_Mas_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Vitro'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    nuevo_producto = models.Vitro_MasVen(
        Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2,
    )
    db_session.add(nuevo_producto)
    db_session.commit()
    return redirect("Vitro_Masvend")

@app.post('/Act_Vitro_Masven/<id>')
def Act_Vitro_Masven(id):
    producto_act = db_session.query(models.Vitro_MasVen).get(id)

    if producto_act is None:
        flash('ID no encontrado')
        return redirect(url_for('Vitro_Masvend'))

    # Obtener los nuevos datos del formulario
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())  # Generar identificador único
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)  # Separar nombre y extensión
            new_filename = f"{unique_id}_{name}{ext}"  # Renombrar el archivo
            try:
                file.save(os.path.join(app.config['IMGS_Mas_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Vitro'], new_filename)  # Retornar la ruta completa
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None  # Retornar None si hubo un error
        else:
            return None  # Retornar None si no hay archivo
    
    # Función para guardar la imagen y manejar eliminación de la antigua
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path)  # Eliminar la imagen antigua
        return new_image_path if new_image_path else current_image_path

    # Actualizar imágenes si se han subido nuevas
    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    # Actualizar otros campos
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt = PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido = Cont_act
    producto_act.Calidad = Cal_act
    
    db_session.add(producto_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Vitro_Masvend'))

# --------------------------- Método de eliminar ---------------------
@app.get('/E_Vitro_Masven/<id>')
def E_Vitro_Masven(id):
   product = db_session.query(models.Vitro_MasVen).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Vitro_Masvend'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Mas_Vend/Vitromex'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Vitro_Masvend')) 

# Rutas para el registro de productos en pisos de Daltile
@app.post('/regDaltile_Masvend')
def regDaltile_Masvend():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_Mas_Daltile'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Daltile'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    nuevo_producto = models.Daltile_MasVen(
        Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2,
    )
    db_session.add(nuevo_producto)
    db_session.commit()
    return redirect("Daltile_Masvend")

@app.post('/Act_Daltile_Masven/<id>')
def Act_Daltile_Masven(id):
    producto_act = db_session.query(models.Daltile_MasVen).get(id)

    if producto_act is None:
        flash('ID no encontrado')
        return redirect(url_for('Daltile_Masvend'))

    # Obtener los nuevos datos del formulario
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())  # Generar identificador único
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)  # Separar nombre y extensión
            new_filename = f"{unique_id}_{name}{ext}"  # Renombrar el archivo
            try:
                file.save(os.path.join(app.config['IMGS_Mas_Daltile'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Daltile'], new_filename)  # Retornar la ruta completa
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None  # Retornar None si hubo un error
        else:
            return None  # Retornar None si no hay archivo
    
    # Función para guardar la imagen y manejar eliminación de la antigua
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path)  # Eliminar la imagen antigua
        return new_image_path if new_image_path else current_image_path

    # Actualizar imágenes si se han subido nuevas
    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    # Actualizar otros campos
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt = PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido = Cont_act
    producto_act.Calidad = Cal_act

    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Daltile_Masvend'))

# --------------------------- Método de eliminar ---------------------
@app.get('/E_Daltile_Masven/<id>')
def E_Daltile_Masven(id):
   product = db_session.query(models.Daltile_MasVen).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Daltile_Masvend'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Mas_Vend/Daltile'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Daltile_Masvend')) 

# Rutas para el registro de productos en pisos de Minato
@app.post('/regMinato_Masvend')
def regMinato_Masvend():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_Mas_Minato'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Minato'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    nuevo_producto = models.Minato_MasVen(
        Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2,
    )
    db_session.add(nuevo_producto)
    db_session.commit()
    return redirect("Minato_Masvend")

@app.post('/Act_Minato_Masven/<id>')
def Act_Minato_Masven(id):
    producto_act = db_session.query(models.Minato_MasVen).get(id)

    if producto_act is None:
        flash('ID no encontrado')
        return redirect(url_for('Minato_Masvend'))

    # Obtener los nuevos datos del formulario
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())  # Generar identificador único
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)  # Separar nombre y extensión
            new_filename = f"{unique_id}_{name}{ext}"  # Renombrar el archivo
            try:
                file.save(os.path.join(app.config['IMGS_Mas_Minato'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Minato'], new_filename)  # Retornar la ruta completa
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None  # Retornar None si hubo un error
        else:
            return None  # Retornar None si no hay archivo
    
    # Función para guardar la imagen y manejar eliminación de la antigua
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path)  # Eliminar la imagen antigua
        return new_image_path if new_image_path else current_image_path

    # Actualizar imágenes si se han subido nuevas
    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    # Actualizar otros campos
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt = PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido = Cont_act
    producto_act.Calidad = Cal_act

    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Minato_Masvend'))

# --------------------------- Método de eliminar ---------------------
@app.get('/E_Minato_Masven/<id>')
def E_Minato_Masven(id):
   product = db_session.query(models.Minato_MasVen).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Minato_Masvend'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Mas_Vend/Minato'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Minato_Masvend')) 

# Rutas para el registro de productos en pisos de vitro
@app.post('/regCastel_Masvend')
def regCastel_Masvend():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_Mas_Castel'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Castel'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    nuevo_producto = models.Castel_MasVen(
        Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2,
    )
    db_session.add(nuevo_producto)
    db_session.commit()
    return redirect("Castel_Masvend")

@app.post('/Act_Castel_Masven/<id>')
def Act_Castel_Masven(id):
    producto_act = db_session.query(models.Castel_MasVen).get(id)

    if producto_act is None:
        flash('ID no encontrado')
        return redirect(url_for('Castel_Masvend'))

    # Obtener los nuevos datos del formulario
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())  # Generar identificador único
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)  # Separar nombre y extensión
            new_filename = f"{unique_id}_{name}{ext}"  # Renombrar el archivo
            try:
                file.save(os.path.join(app.config['IMGS_Mas_Castel'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Castel'], new_filename)  # Retornar la ruta completa
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None  # Retornar None si hubo un error
        else:
            return None  # Retornar None si no hay archivo
    
    # Función para guardar la imagen y manejar eliminación de la antigua
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path)  # Eliminar la imagen antigua
        return new_image_path if new_image_path else current_image_path

    # Actualizar imágenes si se han subido nuevas
    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    # Actualizar otros campos
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt = PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido = Cont_act
    producto_act.Calidad = Cal_act

    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Castel_Masvend'))

# --------------------------- Método de eliminar ---------------------
@app.get('/E_Castel_Masven/<id>')
def E_Castel_Masven(id):
   product = db_session.query(models.Castel_MasVen).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Castel_Masvend'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Mas_Vend/Castel'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Castel_Masvend')) 

# Rutas para el registro de productos en pisos de Greda
@app.post('/regGreda_Masvend')
def regGreda_Masvend():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_Mas_Greda'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Greda'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    nuevo_producto = models.Greda_MasVen(
        Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2,
    )
    db_session.add(nuevo_producto)
    db_session.commit()
    return redirect("Greda_Masvend")

@app.post('/Act_Greda_Masven/<id>')
def Act_Greda_Masven(id):
    producto_act = db_session.query(models.Greda_MasVen).get(id)

    if producto_act is None:
        flash('ID no encontrado')
        return redirect(url_for('Greda_Masvend'))

    # Obtener los nuevos datos del formulario
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())  # Generar identificador único
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)  # Separar nombre y extensión
            new_filename = f"{unique_id}_{name}{ext}"  # Renombrar el archivo
            try:
                file.save(os.path.join(app.config['IMGS_Mas_Greda'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Greda'], new_filename)  # Retornar la ruta completa
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None  # Retornar None si hubo un error
        else:
            return None  # Retornar None si no hay archivo
    
    # Función para guardar la imagen y manejar eliminación de la antigua
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path)  # Eliminar la imagen antigua
        return new_image_path if new_image_path else current_image_path

    # Actualizar imágenes si se han subido nuevas
    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    # Actualizar otros campos
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt = PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido = Cont_act
    producto_act.Calidad = Cal_act

    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Greda_Masvend'))

# --------------------------- Método de eliminar ---------------------
@app.get('/E_Greda_Masven/<id>')
def E_Greda_Masven(id):
   product = db_session.query(models.Greda_MasVen).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Greda_Masvend'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Mas_Vend/Greda'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Greda_Masvend')) 

# Rutas para el registro de productos en pisos de Cesantoni
@app.post('/regCesant_Masvend')
def regCesant_Masvend():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_Mas_Cesant'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Cesant'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    nuevo_producto = models.Cesantoni_MasVen(
        Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2,
    )
    db_session.add(nuevo_producto)
    db_session.commit()
    return redirect("Cesant_Masvend")

@app.post('/Act_Cesant_Masven/<id>')
def Act_Cesant_Masven(id):
    producto_act = db_session.query(models.Cesantoni_MasVen).get(id)

    if producto_act is None:
        flash('ID no encontrado')
        return redirect(url_for('Cesant_Masvend'))

    # Obtener los nuevos datos del formulario
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())  # Generar identificador único
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)  # Separar nombre y extensión
            new_filename = f"{unique_id}_{name}{ext}"  # Renombrar el archivo
            try:
                file.save(os.path.join(app.config['IMGS_Mas_Cesant'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Cesant'], new_filename)  # Retornar la ruta completa
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None  # Retornar None si hubo un error
        else:
            return None  # Retornar None si no hay archivo
    
    # Función para guardar la imagen y manejar eliminación de la antigua
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path)  # Eliminar la imagen antigua
        return new_image_path if new_image_path else current_image_path

    # Actualizar imágenes si se han subido nuevas
    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    # Actualizar otros campos
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt = PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido = Cont_act
    producto_act.Calidad = Cal_act

    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Cesant_Masvend'))

# --------------------------- Método de eliminar ---------------------
@app.get('/E_Cesant_Masven/<id>')
def E_Cesant_Masven(id):
   product = db_session.query(models.Cesantoni_MasVen).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Cesant_Masvend'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Mas_Vend/Cesantoni'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Cesant_Masvend')) 

# Rutas para el registro de productos en pisos de Tecnopiso
@app.post('/regTecno_Masvend')
def regTecno_Masvend():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_Mas_Tecno'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Tecno'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    nuevo_producto = models.Tecno_MasVen(
        Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2,
    )
    db_session.add(nuevo_producto)
    db_session.commit()
    return redirect("Tecno_Masvend")

@app.post('/Act_Tecno_Masven/<id>')
def Act_Tecno_Masven(id):
    producto_act = db_session.query(models.Tecno_MasVen).get(id)

    if producto_act is None:
        flash('ID no encontrado')
        return redirect(url_for('Tecno_Masvend'))

    # Obtener los nuevos datos del formulario
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())  # Generar identificador único
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)  # Separar nombre y extensión
            new_filename = f"{unique_id}_{name}{ext}"  # Renombrar el archivo
            try:
                file.save(os.path.join(app.config['IMGS_Mas_Tecno'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Tecno'], new_filename)  # Retornar la ruta completa
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None  # Retornar None si hubo un error
        else:
            return None  # Retornar None si no hay archivo
    
    # Función para guardar la imagen y manejar eliminación de la antigua
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path)  # Eliminar la imagen antigua
        return new_image_path if new_image_path else current_image_path

    # Actualizar imágenes si se han subido nuevas
    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    # Actualizar otros campos
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt = PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido = Cont_act
    producto_act.Calidad = Cal_act

    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Tecno_Masvend'))

# --------------------------- Método de eliminar ---------------------
@app.get('/E_Tecno_Masven/<id>')
def E_Tecno_Masven(id):
   product = db_session.query(models.Tecno_MasVen).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Tecno_Masvend'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Mas_Vend/Tecnopiso'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Tecno_Masvend')) 

# Rutas para el registro de productos en pisos de Arko
@app.post('/regArko_Masvend')
def regArko_Masvend():
    Nom = request.form['Nombre']
    Prec = request.form['Precio']
    Cod = request.form['Codigo']
    Marc = request.form['Marca']
    PreA = request.form['PrecioAnt']
    Mat = request.form['Material']
    Acab = request.form['Acabado']
    Col = request.form['Color']
    Medi = request.form['Medida']
    Cont = request.form['Contenido']
    Cal = request.form['Calidad']
    
    def save_image(image_field):
        if image_field:
            file = request.files[image_field]
            if file and file.filename != '':
                unique_id = str(uuid.uuid4())  # Generar identificador unico
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)  # Separamos el nombre y extensión
                new_filename = f"{unique_id}_{name}{ext}"  # Renombramos el archivo

                file.save(os.path.join(app.config['IMGS_Mas_Arko'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Arko'], new_filename)
        return None

    Img = save_image('Imagen')
    Img2 = save_image('IMG2')
    nuevo_producto = models.Arko_MasVen(
        Nombre = Nom, Precio = Prec, Codigo = Cod, Marca = Marc, PrecioAnt = PreA, Material = Mat, Acabado = Acab, Color = Col, Medida = Medi, Contenido = Cont, Calidad = Cal, Imagen = Img, IMG2 = Img2,
    )
    db_session.add(nuevo_producto)
    db_session.commit()
    return redirect("Ark_Masvend")

@app.post('/Act_Arko_Masven/<id>')
def Act_Arko_Masven(id):
    producto_act = db_session.query(models.Arko_MasVen).get(id)

    if producto_act is None:
        flash('ID no encontrado')
        return redirect(url_for('Ark_Masvend'))

    # Obtener los nuevos datos del formulario
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())  # Generar identificador único
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)  # Separar nombre y extensión
            new_filename = f"{unique_id}_{name}{ext}"  # Renombrar el archivo
            try:
                file.save(os.path.join(app.config['IMGS_Mas_Arko'], new_filename))
                return os.path.join(app.config['IMGS_Mas_Arko'], new_filename)  # Retornar la ruta completa
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None  # Retornar None si hubo un error
        else:
            return None  # Retornar None si no hay archivo
    
    # Función para guardar la imagen y manejar eliminación de la antigua
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path)  # Eliminar la imagen antigua
        return new_image_path if new_image_path else current_image_path

    # Actualizar imágenes si se han subido nuevas
    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    # Actualizar otros campos
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt = PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Medida = Med_act
    producto_act.Contenido = Cont_act
    producto_act.Calidad = Cal_act

    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Ark_Masvend'))

# --------------------------- Método de eliminar ---------------------
@app.get('/E_Arko_Masven/<id>')
def E_Arko_Masven(id):
   product = db_session.query(models.Arko_MasVen).get(id)
   
   if product == None:
       flash('ID no encontrado')
       return redirect(url_for('Ark_Masvend'))
   
   image_paths = [product.Imagen, product.IMG2]
    
   base_path = 'static/imagenes/Mas_Vend/Arko'

   for image_path in image_paths:
        if image_path:
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')
   
   db_session.delete(product)
   db_session.commit()
   return redirect(url_for('Ark_Masvend'))

#---------------------------------------- Seccion de actualizaciones ---------------------------------------------

@app.post('/Act_Producto/<id>')
def Act_Producto(id):
    producto_act = db_session.query(models.Productos).get(id)

    if producto_act is None:
        flash('ID no encontrado')
        return redirect(url_for('Acceso'))

    # Obtener los nuevos datos del formulario
    Name_act = request.form['Nombre_act']
    Prec_act = request.form['Precio_act']
    PrecAnt_act = request.form['PrecioAnt_act']
    Cod_act = request.form['Codigo_act']
    Marc_act = request.form['Marca_act']
    PreA_act = request.form['PrecioAnt_act']
    Mat_act = request.form['Material_act']
    Acab_act = request.form['Acabado_act']
    Col_act = request.form['Color_act']
    Med_act = request.form['Medida_act']
    Cont_act = request.form['Contenido_act']
    Cal_act = request.form['Calidad_act']

    def save_image(image_field):
        file = request.files.get(image_field)

        if file and file.filename != '':
            unique_id = str(uuid.uuid4())  # Generar identificador único
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)  # Separar nombre y extensión
            new_filename = f"{unique_id}_{name}{ext}"  # Renombrar el archivo
            try:
                file.save(os.path.join(app.config['IMGS_PM_Vitro'], new_filename))
                return os.path.join(app.config['IMGS_PM_Vitro'], new_filename)  # Retornar la ruta completa
            except Exception as e:
                print(f"Error al guardar la imagen: {e}")
                return None  # Retornar None si hubo un error
        else:
            return None  # Retornar None si no hay archivo
    
    # Función para guardar la imagen y manejar eliminación de la antigua
    def update_image(image_field, current_image_path):
        new_image_path = save_image(image_field)
        if new_image_path and current_image_path and os.path.exists(current_image_path):
            os.remove(current_image_path)  # Eliminar la imagen antigua
        return new_image_path if new_image_path else current_image_path

    # Actualizar imágenes si se han subido nuevas
    producto_act.Imagen = update_image('Imagen_act', producto_act.Imagen)
    producto_act.IMG2 = update_image('IMG2_act', producto_act.IMG2)

    # Actualizar otros campos
    producto_act.Nombre = Name_act
    producto_act.Precio = Prec_act
    producto_act.Codigo = Cod_act
    producto_act.Marca = Marc_act
    producto_act.PrecioAnt = PreA_act
    producto_act.Material = Mat_act
    producto_act.Acabado = Acab_act
    producto_act.Color = Col_act
    producto_act.Id_Medida = Med_act
    producto_act.Contenido = Cont_act
    producto_act.Calidad = Cal_act

    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Acceso'))


@app.post('/Act_Admin/<id>')
def Act_Admin(id):
    User_act = db_session.query(models.Admin).get(id)
       
    if User_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Acceso'))

    name = request.form['Nombre_act']
    App_P = request.form['Apellido_P']
    App_M = request.form['Apellido_M']
    us = request.form['Usuario_act']
    
    if User_act == None:
        flash('No hay nada')
        return redirect (url_for('Acceso'))

    User_act.Nombre = name,
    User_act.Apellido_P = App_P,
    User_act.Apellido_M = App_M,
    User_act.Usuario = us,
    
    db_session.add(User_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('Acceso'))



@app.post('/Act_SubAdm/<id>')
def Act_SubAdm(id):
    Sub_user_act = db_session.query(models.SubAdmin).get(id)
       
    if Sub_user_act == None:
        flash('ID no encontrado')
        return redirect (url_for('Acceso'))

    name = request.form['Nombre_act']
    Apps = request.form['Apellidos_act']
    us = request.form['Usuario_act']
    Direc = request.form['Direccion_act']
    
    if Sub_user_act == None:
        flash('No hay nada')
        return redirect (url_for('subAdmins'))

    Sub_user_act.Nombre = name,
    Sub_user_act.Apellidos = Apps,
    Sub_user_act.Usuario = us,
    Sub_user_act.Direccion = Direc,
    
    db_session.add(Sub_user_act)
    db_session.commit()
    flash('Actualización exitosa')
    return redirect(url_for('subAdmins'))

#---------------------------------------------- Sección de Eliminación -------------------------------------

@app.get('/E_Producto/<id>')
def E_Producto(id):
    product = db_session.query(models.Productos).get(id)
    
    if product is None:
        flash('ID no encontrado')
        return redirect(url_for('Acceso'))
    
    image_paths = [product.Imagen, product.IMG2]
    
    # Ruta base donde se almacenan las imágenes
    base_path = 'static/imagenes/Pisos_Muros/Vitromex'

    for image_path in image_paths:
        if image_path:
            # Crear la ruta completa de la imagen
            full_path = os.path.join(base_path, os.path.basename(image_path))  
            
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                    print(f'Imagen {full_path} eliminada con éxito.')
                except OSError as e:
                    print(f'Error al eliminar la imagen {full_path}: {e}')
            else:
                print(f'Imagen {full_path} no encontrada.')

    db_session.delete(product)
    db_session.commit()
    
    return redirect(url_for('Acceso'))


# @app.get('/E_Admin/<id>')
# def E_Admin(id):
#    Adm = db_session.query(models.Admin).get(id)
   
#    if Adm == None:
#        flash('ID no encontrado')
#        return redirect(url_for('Admins'))
   
#    db_session.delete(Adm)
#    db_session.commit()
   
#    return redirect(url_for('Admins'))  

@app.get('/E_Admin/<id>')
def E_Admin(id):
    # Busca al subadministrador en la base de datos
    adm = db_session.query(models.Admin).get(id)

    if adm is None:
        flash('ID no encontrado.')
        return redirect(url_for('Admins'))
    
    # Verifica si el subadministrador está activo, El dato se extrae desde la BD en la columna activo.
    if adm.activo:
        flash("¡Error!, La sesión está activa.")
        return redirect(url_for('Admins'))
    
    # Elimina el subadministrador
    db_session.delete(adm)
    db_session.commit()

    flash(f"El administrador con ID {id} ha sido eliminado.")
    return redirect(url_for('Admins'))


# @app.get('/E_SubAdm/<id>')
# def E_SubAdm(id):
#     ID_sub = session['user_id']
#     sub_adm = db_session.query(models.SubAdmin).get(id)
    
#     if sub_adm == None:
#         flash('ID no encontrado')
#         return redirect(url_for('subAdmins'))
    
#     db_session.delete(sub_adm)
#     db_session.commit()
    
#     return redirect(url_for('subAdmins')) 

@app.get('/E_SubAdm/<id>')
def E_SubAdm(id):
    # Busca al subadministrador en la base de datos
    sub_adm = db_session.query(models.SubAdmin).get(id)

    if sub_adm is None:
        flash('ID no encontrado.')
        return redirect(url_for('subAdmins'))
    
    # Verifica si el subadministrador está activo, El dato se extrae desde la BD en la columna activo.
    if sub_adm.activo:
        flash("¡Error!, La sesión está activa")
        return redirect(url_for('subAdmins'))
    
    # Elimina el subadministrador
    db_session.delete(sub_adm)
    db_session.commit()

    flash(f"El subadministrador ha sido eliminado.")
    return redirect(url_for('subAdmins'))

if __name__ == '__main__':
    app.run('0.0.0.0', 5002, debug=True)