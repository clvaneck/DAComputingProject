    elif meanopacitymodel[0] == 'kramer':
        X = 0.7
        Z = 0.02
        g_ff = 1.0
        const = 3.68 * 1e22 * g_ff * (1.0 - Z) * (1.0 + X)
        mean_opacity_rosseland[:] = const * rhogas * temp**(-3.5)
        mean_opacity_planck[:] = mean_opacity_rosseland[:]

    elif meanopacitymodel[0] == 'es':
        X_value = 0.7
        kappa_es = 0.2 * (1.0 + X_value)
        mean_opacity_planck[:] = kappa_es
        mean_opacity_rosseland[:] = kappa_es

    elif meanopacitymodel[0] == 'combined':
        # Combine Kramer's opacity with electron scattering opacity
        X_value = 0.7
        kappa_es = 0.2 * (1.0 + X_value)
        # Kramer's opacity
        X = 0.7
        Z = 0.02
        g_ff = 1.0
        const = 5e24 * g_ff * (1.0 - Z) * (1.0 + X)
        kappa_kramer = const * rhogas * temp**(-3.5)
        total_kappa = kappa_kramer + kappa_es
        mean_opacity_planck[:] = total_kappa
        mean_opacity_rosseland[:] = total_kappa
