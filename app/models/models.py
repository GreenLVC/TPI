from sqlalchemy import Column, Integer, String, Date, Float, Time, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Artista(Base):
    __tablename__ = 'artistas'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    nombre = Column(String(50), nullable=False)
    popularidad = Column(Float, nullable=False)
    tipo_artista = Column(Integer, nullable=False)

    albums = relationship("Album")
    gen_artist = relationship('GeneroCancion', back_populates='artist_gen')

    def __repr__(self):
        return ' {} {} {} '.format(self.nombre, self.popularidad, self.tipo_artista)


class Album(Base):
    __tablename__ = 'albums'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    nombre = Column(String(75), nullable=False)
    fecha_salida = Column(Date)
    id_artista = Column(Integer, ForeignKey('artistas.id'))
    canciones = relationship("Cancion")

    def __repr__(self):
        return ' {} {} '.format(self.nombre, self.fecha_salida)


class Cancion(Base):
    __tablename__ = 'canciones'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    titulo = Column(String(75), nullable=False)
    pista = Column(String(75), nullable=False)
    mood = Column(String(30), nullable=False)
    duracion = Column(Time, nullable=False)
    reproducciones = Column(Integer, nullable=False)
    explicita = Column(Boolean, nullable=False)
    popularidad = Column(Float, nullable=False)
    tipo_cancion = Column(String(30), nullable=False)
    id_album = Column(Integer, ForeignKey('albums.id'), nullable=True)

    g_cancion = relationship('Cancion', back_populates='cancion_g')
    playl_canciones = relationship('Canciones', back_populates='canciones_playl')

    def __repr__(self):
        return ' {} {} {} {} {} {} {} {}'.format(self.titulo, self.pista, self.mood, self.duracion,
                                                 self.reproducciones, self.explicita, self.popularidad,
                                                 self.tipo_cancion)


class Cuenta(Base):
    __tablename__ = 'cuentas'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    email = Column(String(30))
    explicito = Column(Boolean, nullable=False)
    display_name = Column(String(30), nullable=False)
    tipo_cuenta = Column(Integer, nullable=False)

    cuenta_persona = relationship(Integer, ForeignKey('usuarios.id'))

    def __repr__(self):
        return ' {} {} {} {} '.format(self.email, self.explicito,
                                      self.display_name, self.tipo_cuenta)


class GeneroCancion(Base):
    __tablename__ = 'generos_canciones'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    id_artista = Column(Integer, ForeignKey('artistas.id'), nullable=False)
    id_cancion = Column(Integer, ForeignKey('canciones.id'), nullable=False)
    id_genero = Column(Integer, ForeignKey('generos.id'), nullable=False)
    artista_principal = Column(Integer, nullable=False)
    fecha_publicacion = Column(Date, nullable=False)

    artist_gen = relationship('Artista', back_populates='gen_artist')
    cancion_g = relationship('Cancion', back_populates='g_cancion')
    gener_c = relationship('Genero', back_populates='c_gener')

    def __repr__(self):
        return ' {} {} {} {} {} '.format(self.id_artista, self.id_cancion, self.id_genero,
                                         self.artista_principal, self.fecha_publicacion)


class Genero(Base):
    __tablename__ = 'generos'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    nombre = Column(String(30), nullable=False)
    descripcion = Column(String(75), nullable=True)
    id_sub_genero = Column(Integer, ForeignKey('generos.id'), nullable=True)

    c_gener = relationship('Genero', back_populates='gener_c')

    def __repr__(self):
        return ' {} {} '.format(self.nombre, self.descripcion)


class PlaylistCancion(Base):
    __tablename__ = 'playlists_canciones'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    id_playlist = Column(Integer, ForeignKey('playlists.id'), nullable=False)
    id_cancion = Column(Integer, ForeignKey('canciones.id'), nullable=False)
    total = Column(Integer, nullable=False)
    limite = Column(Integer, nullable=False)

    canciones_playl = relationship('Canciones', back_populates='playl_canciones')

    def __repr__(self):
        return ' {} {} {} {}'.format(self.id_playlist, self.id_cancion, self.total, self.limite)


class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    nombre = Column(String(30), nullable=False)
    fecha_creacion = Column(Date, nullable=False)
    privacidad = Column(Boolean, nullable=False)

    usuario_playlist = relationship('Usuario', back_populates='playlist_usuario')

    def __repr__(self):
        return ' {} {} {} '.format(self.nombre, self.fecha_creacion, self.privacidad)


class UsuarioPlaylist(Base):
    __tablename__ = 'usuarios_playlists'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_playlist = Column(Integer, ForeignKey('playlists.id'), nullable=False)
    tipo_usuario = Column(Integer, nullable=False)
    fecha_uso = Column(Date, nullable=True)
    fecha_modificacion = Column(Date, nullable=True)
    fecha_eliminacion = Column(Date, nullable=True)

    playlist_usuario = relationship('Playlist', back_populates='usuario_playlist')

    def __repr__(self):
        return ' {} {} {} {} {} {} '.format(self.id_usuario, self.id_playlist, self.tipo_usuario,
                                            self.fecha_uso, self.fecha_modificacion,
                                            self.fecha_eliminacion)


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    alias = Column(String(30), nullable=False)
    contrasenia = Column(String(30), nullable=False)
    foto_perfil = Column(String(75), nullable=True)
    pais = Column(Integer, nullable=False)
    id_cuenta = Column(Integer, nullable=False)
    email = Column(String(30), nullable=False)
    cuenta = relationship("Cuenta")

    def __repr__(self):
        return ' {} {} {} {} {} {} '.format(self.alias, self.contrasenia, self.foto_perfil,
                                            self.pais, self.id_cuenta, self.email)
