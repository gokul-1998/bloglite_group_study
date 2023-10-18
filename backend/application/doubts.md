- roles = db.relationship('Role', secondary=roles_users,backref=db.backref('users', lazy='dynamic'))
    - try understanding this

- mnany to nmany relationshi
 @cache.memoize(50) vs     @cache.cached(timeout=50,key_prefix='all-users-present')