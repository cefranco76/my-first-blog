# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dtproperties(models.Model):
    id = models.IntegerField()
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'


class TabAcaoResp(models.Model):
    pk_acao_resp = models.AutoField(primary_key=True)
    dsc_acao_resp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_acao_resp'


class TabAlbum(models.Model):
    pk_album = models.AutoField(primary_key=True)
    ordem = models.IntegerField(blank=True, null=True)
    desc_album = models.CharField(max_length=50, blank=True, null=True)
    fpp = models.IntegerField(blank=True, null=True)
    fotos_adic = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_album'


class TabBanco(models.Model):
    pk_banco = models.AutoField(primary_key=True)
    desc_banco = models.CharField(max_length=50)
    cod_banco = models.IntegerField(blank=True, null=True)
    sigla_banco = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_banco'


class TabBatepapoConversa(models.Model):
    pk_conversa = models.IntegerField()
    id_conversa = models.IntegerField(blank=True, null=True)
    pk_pessoa = models.CharField(max_length=10, blank=True, null=True)
    nome_pessoa = models.CharField(max_length=50, blank=True, null=True)
    dh_conversa = models.DateTimeField(blank=True, null=True)
    dsc_fala = models.CharField(max_length=500, blank=True, null=True)
    sessionid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_batepapo_conversa'


class TabBatepapoPessoa(models.Model):
    pk_pessoa = models.IntegerField()
    nome_pessoa = models.CharField(max_length=50, blank=True, null=True)
    dh_entrada = models.DateTimeField(blank=True, null=True)
    dh_saida = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    sessionid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_batepapo_pessoa'


class TabCobranca(models.Model):
    pk_cobranca = models.AutoField(primary_key=True)
    fk_empresa = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    data_ticket = models.DateTimeField(blank=True, null=True)
    data_venc = models.DateTimeField(blank=True, null=True)
    baixa = models.IntegerField(blank=True, null=True)
    data_ini = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    fk_plano = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_cobranca'


class TabComentario(models.Model):
    pk_comentario = models.IntegerField()
    fk_imagem = models.IntegerField(blank=True, null=True)
    fk_evento = models.IntegerField(blank=True, null=True)
    dh_comentario = models.DateTimeField()
    ip = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    dsc_comentario = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'tab_comentario'


class TabContatoRegistro(models.Model):
    pk_registro = models.AutoField(primary_key=True)
    dh_registro = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    assunto = models.CharField(max_length=500, blank=True, null=True)
    mensagem = models.CharField(max_length=4000, blank=True, null=True)
    lido = models.IntegerField(blank=True, null=True)
    resp = models.IntegerField(blank=True, null=True)
    lixo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_contato_registro'


class TabContent(models.Model):
    pk_content = models.AutoField(primary_key=True)
    fk_idioma = models.IntegerField(blank=True, null=True)
    id_content = models.CharField(max_length=50, blank=True, null=True)
    desc_content = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_content'


class TabContratoEstagio(models.Model):
    pk_contrato_estagio = models.AutoField(primary_key=True)
    ordem = models.IntegerField(blank=True, null=True)
    desc_contrato_estagio = models.CharField(max_length=100, blank=True, null=True)
    flag_album = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_contrato_estagio'


class TabContratoHistorico(models.Model):
    pk_status_historico = models.AutoField(primary_key=True)
    fk_contrato = models.IntegerField(blank=True, null=True)
    dh_status = models.DateTimeField(blank=True, null=True)
    fk_contrato_status = models.IntegerField(blank=True, null=True)
    prazo_dias = models.IntegerField(blank=True, null=True)
    observacoes = models.CharField(max_length=180, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_contrato_historico'


class TabContratoStatus(models.Model):
    pk_contrato_status = models.AutoField(primary_key=True)
    ativo = models.IntegerField(blank=True, null=True)
    fk_empresa = models.IntegerField(blank=True, null=True)
    ordem_contrato_status = models.IntegerField()
    desc_contrato_status = models.CharField(max_length=50)
    fk_contrato_estagio = models.IntegerField(blank=True, null=True)
    impresso = models.IntegerField(blank=True, null=True)
    fk_acao_resp = models.IntegerField()
    prazo_dias = models.IntegerField(blank=True, null=True)
    flag_envio_sms = models.IntegerField(blank=True, null=True)
    string_sms1 = models.CharField(max_length=100, blank=True, null=True)
    string_sms2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_contrato_status'


class TabContratos(models.Model):
    pk_contrato = models.AutoField(primary_key=True)
    data_contrato = models.DateTimeField(blank=True, null=True)
    nome_completo = models.CharField(max_length=250, blank=True, null=True)
    rg = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(max_length=50, blank=True, null=True)
    cnpj = models.CharField(max_length=50, blank=True, null=True)
    insc_estadual = models.CharField(max_length=50, blank=True, null=True)
    insc_municipal = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=250, blank=True, null=True)
    compl = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=150, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    cidade = models.CharField(max_length=250, blank=True, null=True)
    telefone_com = models.CharField(max_length=20, blank=True, null=True)
    telefone_cel = models.CharField(max_length=20, blank=True, null=True)
    telefone_cel2 = models.CharField(max_length=20, blank=True, null=True)
    telefone_res = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)
    data_evento = models.DateTimeField(blank=True, null=True)
    horario = models.CharField(max_length=50, blank=True, null=True)
    qtde_convidados = models.IntegerField(blank=True, null=True)
    tipo_evento = models.IntegerField(blank=True, null=True)
    id_tipo_evento = models.IntegerField(blank=True, null=True)
    nome_noiva = models.CharField(max_length=250, blank=True, null=True)
    nome_noivo = models.CharField(max_length=250, blank=True, null=True)
    nome_debutante = models.CharField(max_length=250, blank=True, null=True)
    nome_aniversario = models.CharField(max_length=250, blank=True, null=True)
    nome_dependente = models.CharField(max_length=250, blank=True, null=True)
    local_cerimonia = models.CharField(max_length=250, blank=True, null=True)
    endereco_cerimonia = models.CharField(max_length=250, blank=True, null=True)
    makingof = models.IntegerField(blank=True, null=True)
    local_makingof = models.CharField(max_length=250, blank=True, null=True)
    externas = models.IntegerField(blank=True, null=True)
    local_externas = models.CharField(max_length=250, blank=True, null=True)
    local_festa = models.CharField(max_length=250, blank=True, null=True)
    endereco_festa = models.CharField(max_length=250, blank=True, null=True)
    tamanho_album = models.CharField(max_length=50, blank=True, null=True)
    qtde_paginas = models.IntegerField(blank=True, null=True)
    cor_album = models.CharField(max_length=50, blank=True, null=True)
    valor = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    qtde_parcelas = models.IntegerField(blank=True, null=True)
    valor_obs = models.CharField(max_length=2000, blank=True, null=True)
    anexo = models.CharField(max_length=2000, blank=True, null=True)
    fk_usuario = models.IntegerField(blank=True, null=True)
    fk_evento = models.IntegerField(blank=True, null=True)
    duracao = models.IntegerField(blank=True, null=True)
    fk_contrato_status = models.IntegerField()
    acab_luxo = models.IntegerField(blank=True, null=True)
    foto_capa = models.IntegerField(blank=True, null=True)
    banner = models.IntegerField(blank=True, null=True)
    caixa_album = models.CharField(max_length=60, blank=True, null=True)
    tipo_equipe = models.IntegerField(blank=True, null=True)
    qtde_fotografos = models.IntegerField(blank=True, null=True)
    album = models.IntegerField(blank=True, null=True)
    fk_empresa = models.IntegerField(blank=True, null=True)
    fotos_aprovar = models.IntegerField(blank=True, null=True)
    material_impresso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_contratos'


class TabEmail(models.Model):
    pk_email = models.AutoField(primary_key=True)
    dh_envio = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    apelido = models.CharField(max_length=50, blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    dia = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    aniv = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    dh_leitura = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_email'


class TabEmailTipo(models.Model):
    pk_email_tipo = models.AutoField(primary_key=True)
    desc_email_tipo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_email_tipo'


class TabEmpresas(models.Model):
    pk_empresa = models.ForeignKey('self', models.DO_NOTHING, db_column='pk_empresa', primary_key=True)
    fk_usuario_origem = models.IntegerField(blank=True, null=True)
    fk_usuario = models.IntegerField(blank=True, null=True)
    nome_empresa = models.CharField(max_length=100, blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)
    tipo_empresa = models.IntegerField(blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    responsavel = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    endereco = models.CharField(max_length=500, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    cidade = models.CharField(max_length=250, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    fk_plano_lixo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_empresas'


class TabEventos(models.Model):
    pk_evento = models.AutoField(primary_key=True)
    fk_empresa = models.IntegerField(blank=True, null=True)
    fk_contrato = models.IntegerField(blank=True, null=True)
    fk_usuario = models.IntegerField(blank=True, null=True)
    titulo_evento = models.CharField(max_length=250, blank=True, null=True)
    desc_evento = models.CharField(max_length=250, blank=True, null=True)
    data_evento = models.DateTimeField(blank=True, null=True)
    desc_local = models.CharField(max_length=500, blank=True, null=True)
    desc_endereco_evento = models.CharField(max_length=500, blank=True, null=True)
    cidade = models.CharField(max_length=80, blank=True, null=True)
    vlr_custo_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_fat_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fechado = models.CharField(max_length=50, blank=True, null=True)
    path_album = models.CharField(max_length=200, blank=True, null=True)
    ft_decoracao = models.CharField(max_length=350, blank=True, null=True)
    ft_cerimonial = models.CharField(max_length=350, blank=True, null=True)
    ft_buffet = models.CharField(max_length=350, blank=True, null=True)
    ft_banda = models.CharField(max_length=350, blank=True, null=True)
    observacao = models.CharField(max_length=300, blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    path_fotos = models.CharField(max_length=200, blank=True, null=True)
    download_permitido = models.IntegerField(blank=True, null=True)
    ordem_imagens = models.IntegerField(blank=True, null=True)
    tipo_conteudo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_eventos'


class TabImagens(models.Model):
    pk_imagem = models.AutoField(primary_key=True)
    fk_evento = models.IntegerField(blank=True, null=True)
    titulo_imagem = models.CharField(max_length=50, blank=True, null=True)
    desc_imagem = models.CharField(max_length=50, blank=True, null=True)
    caminho_thumb = models.CharField(max_length=250, blank=True, null=True)
    caminho_imagem = models.CharField(max_length=250, blank=True, null=True)
    dimensoes_imagem = models.CharField(max_length=50, blank=True, null=True)
    sugerida = models.IntegerField(blank=True, null=True)
    sugerida_cliente = models.IntegerField(blank=True, null=True)
    recusada = models.IntegerField(blank=True, null=True)
    aprovada = models.IntegerField(blank=True, null=True)
    ocultar = models.IntegerField(blank=True, null=True)
    tipo_uso = models.IntegerField(blank=True, null=True)
    efeito_foto = models.IntegerField(blank=True, null=True)
    efeito_sep = models.IntegerField(blank=True, null=True)
    number_3d = models.IntegerField(db_column='3d', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    anaglifo = models.IntegerField(blank=True, null=True)
    pk_imagem_hash = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_imagens'


class TabLanguage(models.Model):
    pk_idioma = models.AutoField(primary_key=True)
    cod_idioma = models.CharField(max_length=50)
    desc_idioma = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tab_language'


class TabLogsystem(models.Model):
    pk_logsystem = models.AutoField()
    dh_logsystem = models.DateTimeField()
    fk_tipolog = models.IntegerField(blank=True, null=True)
    fk_usuario = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    desc_pagina = models.CharField(max_length=300, blank=True, null=True)
    fk_evento = models.IntegerField(blank=True, null=True)
    fk_imagem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_logsystem'


class TabMensagemSms(models.Model):
    pk_mensagem_sms = models.AutoField(primary_key=True)
    dh_mensagem_sms = models.DateTimeField(blank=True, null=True)
    dispatcher_id = models.IntegerField(blank=True, null=True)
    nro_remetente = models.CharField(max_length=50, blank=True, null=True)
    ind_status = models.CharField(max_length=10, blank=True, null=True)
    cod_envio = models.IntegerField(blank=True, null=True)
    nro_la = models.IntegerField(blank=True, null=True)
    msg = models.CharField(max_length=50, blank=True, null=True)
    des_operadora = models.CharField(max_length=50, blank=True, null=True)
    fk_contrato = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_mensagem_sms'


class TabOrcamentoDetalhe(models.Model):
    pk_orcamento_detalhe = models.IntegerField()
    fk_orcamento = models.CharField(max_length=10, blank=True, null=True)
    dsc_item_orcamento = models.CharField(max_length=50, blank=True, null=True)
    custo = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    valor = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_orcamento_detalhe'


class TabOrcamentoItem(models.Model):
    pk_orc_item = models.IntegerField()
    dsc_orc_item = models.CharField(max_length=50, blank=True, null=True)
    custo_orc_item = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    valor_orc_item = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_orcamento_item'


class TabOrcamentos(models.Model):
    pk_orcamento = models.IntegerField()
    dh_orcamento = models.DateTimeField(blank=True, null=True)
    nome_completo = models.CharField(max_length=50, blank=True, null=True)
    dh_evento = models.DateTimeField(blank=True, null=True)
    local_evento = models.CharField(max_length=50, blank=True, null=True)
    qtde_convidados = models.IntegerField(blank=True, null=True)
    fk_tipo_evento = models.IntegerField(blank=True, null=True)
    album1 = models.IntegerField(blank=True, null=True)
    album2 = models.IntegerField(blank=True, null=True)
    album3 = models.IntegerField(blank=True, null=True)
    qtde_paginas = models.IntegerField(blank=True, null=True)
    duracao = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cerimonia = models.IntegerField(blank=True, null=True)
    externas = models.IntegerField(blank=True, null=True)
    recepcao = models.IntegerField(blank=True, null=True)
    makingof = models.IntegerField(blank=True, null=True)
    observacoes = models.CharField(max_length=500, blank=True, null=True)
    promocoes = models.CharField(max_length=500, blank=True, null=True)
    email_cliente = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_orcamentos'


class TabPeriodoCobranca(models.Model):
    pk_periodo_cobranca = models.AutoField(primary_key=True)
    periodo = models.IntegerField(blank=True, null=True)
    desc_periodo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_periodo_cobranca'


class TabPgto(models.Model):
    pk_pgto = models.ForeignKey('self', models.DO_NOTHING, db_column='pk_pgto', primary_key=True)
    fk_contrato = models.ForeignKey(TabContratos, models.DO_NOTHING, db_column='fk_contrato')
    fk_pgto_tipo = models.ForeignKey('TabPgtoTipo', models.DO_NOTHING, db_column='fk_pgto_tipo')
    fk_banco = models.IntegerField(blank=True, null=True)
    ag_conta = models.CharField(max_length=50, blank=True, null=True)
    cheque_numero = models.CharField(max_length=50, blank=True, null=True)
    data = models.DateField()
    valor = models.DecimalField(max_digits=18, decimal_places=2)
    flag_pago = models.IntegerField()
    num_parcela = models.IntegerField(blank=True, null=True)
    total_parcelas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_pgto'


class TabPgtoTipo(models.Model):
    pk_pgto_tipo = models.AutoField(primary_key=True)
    desc_pgto_tipo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tab_pgto_tipo'


class TabPlano(models.Model):
    pk_plano = models.AutoField(primary_key=True)
    periodo = models.IntegerField(blank=True, null=True)
    desc_periodo = models.CharField(max_length=50, blank=True, null=True)
    desc_plano = models.CharField(max_length=150, blank=True, null=True)
    qtde_imagens = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    uso = models.IntegerField(blank=True, null=True)
    limite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_plano'


class TabTipoEvento(models.Model):
    pk_tipo_evento = models.AutoField(primary_key=True)
    id_tipo_evento = models.IntegerField(blank=True, null=True)
    dsc_tipo_evento = models.CharField(max_length=50, blank=True, null=True)
    dsc_pt_br = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_tipo_evento'


class TabTipoUsuario(models.Model):
    pk_tipo_usuario = models.AutoField(primary_key=True)
    desc_tipo_usuario = models.CharField(max_length=50, blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_tipo_usuario'


class TabTipolog(models.Model):
    pk_tipolog = models.AutoField(primary_key=True)
    desc_log = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_tipolog'


class TabUsuario(models.Model):
    pk_usuario = models.AutoField(primary_key=True)
    fk_empresa = models.ForeignKey(TabEmpresas, models.DO_NOTHING, db_column='fk_empresa', blank=True, null=True)
    usuario = models.CharField(max_length=200)
    senha = models.CharField(max_length=50)
    fk_tipo_usuario = models.IntegerField(blank=True, null=True)
    nivel = models.IntegerField()
    nome_completo = models.CharField(max_length=80, blank=True, null=True)
    apelido = models.CharField(max_length=50, blank=True, null=True)
    mostra_dicas = models.IntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    telefone_com = models.CharField(max_length=50, blank=True, null=True)
    telefone_cel = models.CharField(max_length=50, blank=True, null=True)
    flag_sms = models.IntegerField(blank=True, null=True)
    telefone_res = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)
    fb_userid2 = models.IntegerField(blank=True, null=True)
    fb_userid = models.CharField(max_length=50, blank=True, null=True)
    senha_velha = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_usuario'
        unique_together = (('pk_usuario', 'usuario'),)
