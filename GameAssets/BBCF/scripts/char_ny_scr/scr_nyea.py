@State
def EMB_NY():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_NY.DIG', 'ef_emb_NY_motion_000.mmot')
        RenderLayer(5)
        BlendMode_Add()
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4294967295, 10)
    sprite('null', 15)
    sprite('null', 15)
    ColorTransition(4286625023, 10)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(200)


@State
def EMB_NY_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_NY.DIG', 'ef_emb_NY_motion_000.mmot')
        RenderLayer(5)
        BlendMode_Add()
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 15)
    sprite('null', 15)
    ColorTransition(4278223103, 10)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(200)


@State
def EMB_NY_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_NY.DIG', 'ef_emb_NY_motion_000.mmot')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4294948020, 10)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 20)


@State
def DIST_NY5D():

    def upon_EVERY_FRAME():
        ParticleTransparency(1)
        PlayerTransparency(20000)
        Unknown3059(-1000)
        E0EAEffectRotation(2)
    sprite('vrdist_ny00', 6)
    SetScaleX(800)
    SetScaleY(600)
    SetScaleXPerFrame(150)
    SetScaleSpeedY(100)
    sprite('vrdist_ny00', 10)
    SetScaleSpeedY(-100)


@State
def DIST_NY5DADD():

    def upon_EVERY_FRAME():
        ParticleTransparency(1)
        PlayerTransparency(20000)
        Unknown3059(-1000)
        RotationAngle(36000)
    sprite('vrdist_ny00', 6)
    SetScaleX(800)
    SetScaleY(600)
    SetScaleXPerFrame(150)
    SetScaleSpeedY(100)
    sprite('vrdist_ny00', 10)
    SetScaleSpeedY(-100)


@State
def DIST_TriSwd():

    def upon_EVERY_FRAME():
        ParticleTransparency(1)
        PlayerTransparency(20000)
        Unknown3059(-1000)
    sprite('vrdist_ny00', 6)
    SetScaleX(1600)
    SetScaleY(1800)
    SetScaleXPerFrame(150)
    SetScaleSpeedY(150)
    sprite('vrdist_ny00', 10)
    SetScaleXPerFrame(-200)


@State
def NY_SummonA():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_sumA03', -1)
    ParticleColorFromPalette(229, 225, 229)
    CallCustomizableParticle('nyef_sumA', -1)
    if random_(2, 0, 33):
        PrivateSE('nyse_23')
    elif random_(2, 0, 50):
        PrivateSE('nyse_24')
    else:
        PrivateSE('nyse_25')


@State
def NY_SummonDmc():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_dmc00', -1)
    ParticleColorFromPalette(229, 226, 229)
    CallCustomizableParticle('nyef_dmc', -1)


@State
def NY_SummonAirDmc():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_airdmc00', -1)
    ParticleColorFromPalette(229, 226, 229)
    CallCustomizableParticle('nyef_airdmc', -1)


@State
def NY_SlowMc():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_slowmc01', -1)
    ParticleColorFromPalette(229, 225, 229)
    CallCustomizableParticle('nyef_slowmc', -1)


@State
def NY_SlowHand():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_slowhand01', -1)
    ParticleColorFromPalette(225, 225, 231)
    CallCustomizableParticle('nyef_slowhandcircle00', -1)
    ParticleColorFromPalette(225, 225, 226)
    CallCustomizableParticle('nyef_slowhand', -1)


@State
def NY_SumMultiSwordBigmc():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_sumDDstart00', -1)
    ParticleColorFromPalette(229, 225, 229)
    CallCustomizableParticle('nyef_sumDDstart01', -1)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('nyef_sumDDstart02', -1)
    ParticleColorFromPalette(226, 225, 226)
    CallCustomizableParticle('nyef_sumDDstart03', -1)
    CallCustomizableParticle('nyef_sumDDstart', -1)


@State
def NY_SumMultiSwordBigmcOD():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
        ParticleColorFromPalette(226, 225, 226)
        CallPrivateEffect('rmef_sumDDstart03b')
    sprite('null', 1000)
    CreateObject('NY_MultiSwordODSub', -1)
    CreateObject('NY_MultiSwordODSub2', -1)
    CreateObject('NY_MultiSwordODSub3', -1)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    TriggerUponForState('NY_MultiSwordODSub', 32)
    TriggerUponForState('NY_MultiSwordODSub2', 32)
    TriggerUponForState('NY_MultiSwordODSub3', 32)


@State
def NY_MultiSwordODSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    LinkParticle('rmef_sumDDstart00')
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def NY_MultiSwordODSub2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    ParticleColorFromPalette(229, 225, 229)
    CallPrivateEffect('nyef_sumDDstart01')
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def NY_MultiSwordODSub3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    ParticleColorFromPalette(226, 226, 226)
    CallPrivateEffect('rmef_sumDDstart02')
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def NY_SumMultiSwordMc():
    PaletteIndex(1)
    sprite('null', 2)
    CreateParticle('nyef_sumDDlaser01', -1)
    ParticleColorFromPalette(225, 225, 226)
    CallCustomizableParticle('nyef_sumDDlaser', -1)


@State
def NY_SumBigSword():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        WallCollisionDetection(1)
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_sumDD03', -1)
    ParticleSize(2000)
    ParticleColorFromPalette(229, 225, 229)
    CallCustomizableParticle('nyef_sumDD', -1)


@State
def NY_SlowFieldStart():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_slowfieldstart', -1)
    ParticleColorFromPalette(226, 227, 226)
    CallCustomizableParticle('nyef_slowmagic', -1)
    ParticleColorFromPalette(229, 230, 229)
    CallCustomizableParticle('nyef_slowmagicloop', -1)


@State
def NY_SlowField():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_slowlight', -1)
    CreateParticle('nyef_slowfieldloop', -1)
    ParticleColorFromPalette(229, 230, 229)
    CallCustomizableParticle('nyef_slowmagicloop', -1)


@State
def NY_ActP2_Down():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddX(32000)
        AddY(0)
        LinkParticle('nyef_act2_down')
        AlphaValue(255)
    sprite('null', 200)
    ConstantAlphaModifier(-5)


@State
def NY_ActP2_Up():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddX(104000)
        AddY(220000)
        LinkParticle('nyef_act2_up')
        AlphaValue(255)
    sprite('null', 200)
    ConstantAlphaModifier(-5)


@State
def NY_MagicA():
    sprite('null', 200)
    CreateParticle('nyef_mcircle', -1)


@State
def SummonSlowArea():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)

        def upon_32():
            AddX(300000)

        def upon_33():
            AddX(700000)

        def upon_34():
            AddX(1100000)

        def upon_35():
            CreateParticle('nyef_slowfieldend', -1)
            DeleteObject(23)
        RunLoopUpon(17, 180)

        def upon_17():
            sendToLabel(1)

        def upon_STATE_END():
            pass
    sprite('null', 1)
    sprite('null', 20)
    CreateObject('NY_SlowFieldStart', -1)
    PrivateSE('nyse_02')
    SlowField(1)
    label(0)
    sprite('null', 20)
    CreateObject('NY_SlowField', -1)
    CommonSE('022_magiccircle_c')
    sprite('null', 20)
    CreateObject('NY_SlowField', -1)
    sprite('null', 20)
    CreateObject('NY_SlowField', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 20)
    CreateParticle('nyef_slowfieldend', -1)


@Subroutine
def DriveSwordInit():
    AttackDefaults_Projectile()
    AutoHitStopSending(1)
    AttackLevel_(4)
    ProjectileLevel(2)
    Damage(600)
    AttackP1(80)
    Blockstun(16)
    Hitstun(17)
    AirUntechableTime(17)
    PushbackX(19800)
    Hitstop(4)
    EnemyHitstopAddition(5, 5, 10)
    UseSlashHitspark(1)
    HitsparkSize(600)
    StarterRating(2)
    CopyFromRightToLeft(23, 2, 58, 3, 2, 58)
    if SLOT_58:
        ChipPercentage(5)

    def upon_32():
        SetActionMark(1)

    def upon_33():
        AutoHitStopSending(0)
        SetActionMark(1)
    PaletteIndex(1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)
    uponSendToLabel(LANDING, 1)

    def upon_OPPONENT_HIT_OR_BLOCK():
        CreateParticle('nyef_breakA', 101)
        CopyFromRightToLeft(3, 2, 59, 25, 2, 83)
        CopyFromRightToLeft(3, 2, 60, 25, 2, 23)
        ObjectUpon(LANDING, 41)
    HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)
    uponSendToLabel(54, 580)


@Subroutine
def DriveSwordLandingParam():
    AttackOff()
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    BlendMode_Normal()
    AlphaValue(250)
    ConstantAlphaModifier(-20)
    CreateObject('NY_MagicA', -1)
    CreateObject('DIST_NY5D', -1)


@Subroutine
def DriveSwordBreakParam():
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    BlendMode_Normal()
    AlphaValue(250)
    ConstantAlphaModifier(-20)
    CreateObject('NY_MagicA', -1)
    CreateObject('DIST_NY5D', -1)


@State
def NY_Sword5D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        AddX(230000)
        AddY(180000)
        physicsXImpulse(25000)
        physicsYImpulse(0)
        RotationSomething(0)
        AirPushbackY(16000)
        AirPushbackX(3000)
    sprite('vrnyef_swda00', 2)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swda01', 2)
    sprite('vrnyef_swda02', 2)
    sprite('vrnyef_swda03', 2)
    sprite('vrnyef_swda04', 2)
    sprite('vrnyef_swda05', 2)
    sprite('vrnyef_swdaatk', 7)
    if not SLOT_2:
        ProjectileLevel(1)
    XImpulseAcceleration(315)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_Sword5DEntryVsRg():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        SetZVal(-500)

    def upon_EVERY_FRAME():
        if SLOT_19 < 260000:
            sendToLabel(580)
    sprite('vrnyef_swda00', 2)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swda01', 2)
    sprite('vrnyef_swda02', 2)
    sprite('vrnyef_swda03', 2)
    sprite('vrnyef_swda04', 2)
    sprite('vrnyef_swda05', 2)
    sprite('vrnyef_swdaatk', 120)
    RefreshMultihit()
    XImpulseAcceleration(315)
    loopRest()
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    clearUponHandler(EVERY_FRAME)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')
    ParticleColor(4278223103, 4278202623, 4278190335)
    if not SLOT_51:
        ParticleFacing(1)
    CallCustomizableParticle('ef_girdm', 0)
    ScreenShake(8000, 2000)
    CommonSE('105_guard_slash_2')
    ObjectUpon(LANDING, 33)
    loopRest()


@State
def NY_Sword6D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        AddX(150000)
        AddY(300000)
        physicsXImpulse(31200)
        physicsYImpulse(6300)
        RotationSomething(0)
    sprite('vrnyef_swdb00', 2)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swdb01', 2)
    sprite('vrnyef_swdb02', 1)
    sprite('vrnyef_swdb03', 1)
    sprite('vrnyef_swdb04', 1)
    sprite('vrnyef_swdb05', 1)
    sprite('vrnyef_swdb06', 1)
    sprite('vrnyef_swdbatk', 10)
    if not SLOT_2:
        ProjectileLevel(1)
    XImpulseAcceleration(420)
    YAccel(420)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_Sword2D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        AddX(130000)
        AddY(330000)
        physicsXImpulse(33000)
        physicsYImpulse(26000)
        RotationSomething(0)
        AirHitstunAnimation(13)
    sprite('vrnyef_swdc00', 1)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swdc01', 1)
    sprite('vrnyef_swdc02', 1)
    sprite('vrnyef_swdc03', 1)
    sprite('vrnyef_swdc04', 1)
    sprite('vrnyef_swdc05', 1)
    sprite('vrnyef_swdc06', 1)
    sprite('vrnyef_swdc07', 1)
    sprite('vrnyef_swdc08', 1)
    sprite('vrnyef_swdcatk', 6)
    if not SLOT_2:
        ProjectileLevel(1)
    XImpulseAcceleration(320)
    YAccel(320)
    SetScaleSpeed(100)
    sprite('vrnyef_swdcatk', 4)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_Sword4D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        ProjectileLevel(1)
        AttackP1(70)
        BonusProration(110)
        PushbackX(-19800)
        AirPushbackX(0)
        AirPushbackY(16000)
        GroundedHitstunAnimation(3)
        HitOverhead(2)
        AttackOff()
        FatalCounter(1)

        def upon_34():
            if SLOT_19 > 600000:
                TeleportToObject(22)
                AddX(150000)
            else:
                AddX(600000)
                AddX(150000)
            AbsoluteY(580000)
            CreateObject('NY_SummonA', 0)
            physicsXImpulse(-1666)
            physicsYImpulse(-4333)
            RotationSomething(0)

        def upon_35():
            ProjectileLevel(2)
            TeleportToObject(22)
            AddX(100000)
            AbsoluteY(580000)
            CreateObject('NY_SummonA', 0)
            physicsXImpulse(-1666)
            physicsYImpulse(-4333)
            RotationSomething(0)

        def upon_36():
            ProjectileLevel(2)
            AutoHitStopSending(0)
            TeleportToObject(22)
            AddX(250000)
            AbsoluteY(330000)
            CreateObject('NY_SummonA', 0)
            physicsXImpulse(-4166)
            physicsYImpulse(-1733)
            RotationSomething(0)
    sprite('vrnyef_swdd00', 6)
    sprite('vrnyef_swdd01', 3)
    sprite('vrnyef_swdd02', 3)
    sprite('vrnyef_swdd03', 3)
    sprite('vrnyef_swdd04', 3)
    sprite('vrnyef_swdd05', 3)
    sprite('vrnyef_swddatk', 2)
    XImpulseAcceleration(1430)
    YAccel(1430)
    sprite('vrnyef_swddatk', 3)
    RefreshMultihit()
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_SwordAirD():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        AddX(240000)
        AddY(280000)
        physicsXImpulse(41400)
        physicsYImpulse(5760)
        RotationSomething(0)
    sprite('vrnyef_swde00', 1)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swde01', 1)
    sprite('vrnyef_swde02', 1)
    sprite('vrnyef_swde03', 1)
    sprite('vrnyef_swde04', 1)
    sprite('vrnyef_swde05', 1)
    sprite('vrnyef_swdeatk', 2)
    XImpulseAcceleration(180)
    YAccel(180)
    sprite('vrnyef_swdeatk', 8)
    if not SLOT_2:
        ProjectileLevel(1)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_SwordAir2D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        AddX(240000)
        AddY(120000)
        physicsXImpulse(19200)
        physicsYImpulse(-12800)
        RotationSomething(0)
    sprite('vrnyef_swde00', 1)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swde01', 1)
    sprite('vrnyef_swde02', 1)
    sprite('vrnyef_swde03', 1)
    sprite('vrnyef_swde04', 1)
    sprite('vrnyef_swde05', 1)
    sprite('vrnyef_swdeatk', 2)
    XImpulseAcceleration(160)
    YAccel(160)
    sprite('vrnyef_swdeatk', 6)
    if not SLOT_2:
        ProjectileLevel(1)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_SwordAir6D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        AddX(240000)
        AddY(180000)
        physicsXImpulse(36800)
        physicsYImpulse(-3200)
        RotationSomething(0)
    sprite('vrnyef_swde00', 1)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swde01', 1)
    sprite('vrnyef_swde02', 1)
    sprite('vrnyef_swde03', 1)
    sprite('vrnyef_swde04', 1)
    sprite('vrnyef_swde05', 1)
    sprite('vrnyef_swdeatk', 2)
    XImpulseAcceleration(160)
    YAccel(160)
    sprite('vrnyef_swdeatk', 4)
    if not SLOT_2:
        ProjectileLevel(1)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_Sword5DAdd():
    sprite('null', 5)
    sprite('null', 1)
    AddX(-130000)
    AddY(80000)
    CreateObject('NY_Sword5D', -1)
    ObjectUpon(STATE_END, 33)


@State
def NY_Sword6DAdd():
    sprite('null', 5)
    sprite('null', 1)
    AddX(-80000)
    AddY(50000)
    CreateObject('NY_Sword6D', -1)
    ObjectUpon(STATE_END, 33)


@State
def NY_Sword2DAdd():
    sprite('null', 5)
    sprite('null', 1)
    AddX(-80000)
    AddY(20000)
    CreateObject('NY_Sword2D', -1)
    ObjectUpon(STATE_END, 33)


@State
def NY_Sword4DAdd():
    sprite('null', 5)
    sprite('null', 1)
    CreateObject('NY_Sword4D', -1)
    ObjectUpon(STATE_END, 36)


@State
def NY_SwordAir5DAdd():
    sprite('null', 5)
    sprite('null', 1)
    AddX(-120000)
    AddY(-80000)
    CreateObject('NY_SwordAirD', -1)
    ObjectUpon(STATE_END, 33)


@State
def NY_SwordAir2DAdd():
    sprite('null', 5)
    sprite('null', 1)
    AddX(-120000)
    AddY(-80000)
    CreateObject('NY_SwordAir2D', -1)
    ObjectUpon(STATE_END, 33)


@State
def NY_SwordAir6DAdd():
    sprite('null', 5)
    sprite('null', 1)
    AddX(-120000)
    AddY(80000)
    CreateObject('NY_SwordAir6D', -1)
    ObjectUpon(STATE_END, 33)


@State
def NY_SwordDChain():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(4)
        Damage(300)
        AttackP1(80)
        Blockstun(20)
        AirUntechableTime(25)
        Hitstun(23)
        Hitstop(4)
        EnemyHitstopAddition(4, 4, 9)
        HitsparkSize(600)
        UseSlashHitspark(1)
        StarterRating(2)
        AutoHitStopSending(1)
        AttackOff()
        CopyFromRightToLeft(23, 2, 58, 3, 2, 58)
        if SLOT_58:
            ChipPercentage(5)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CopyFromRightToLeft(23, 2, 83, 3, 2, 59)
        CopyFromRightToLeft(23, 2, 23, 3, 2, 60)
        CancelIfPlayerHit(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateParticle('nyef_breakA', 101)
            ObjectUpon(LANDING, 41)
        uponSendToLabel(LANDING, 1)

        def upon_32():
            AirHitstunAnimation(10)
            PushbackX(19800)
            AirPushbackY(20000)
            AddX(-200000)
            AddY(400000)
            physicsXImpulse(20000)
            physicsYImpulse(-9000)
            SetAcceleration(2000)
            setGravity(900)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_33():
            AirHitstunAnimation(18)
            PushbackX(12000)
            AirPushbackX(-8000)
            AddX(160000)
            AddY(-100000)
            physicsXImpulse(-3500)
            physicsYImpulse(18000)
            SetAcceleration(-350)
            setGravity(-1800)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_34():
            AirHitstunAnimation(11)
            PushbackX(-19800)
            AirPushbackX(-12000)
            AirPushbackY(32000)
            AddX(300000)
            AddY(50000)
            physicsXImpulse(-20000)
            physicsYImpulse(10000)
            SetAcceleration(-2000)
            setGravity(-1000)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_35():
            AirPushbackY(0)
            AddX(-200000)
            AddY(400000)
            physicsXImpulse(12500)
            physicsYImpulse(-5000)
            SetAcceleration(2500)
            setGravity(1000)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_36():
            AirHitstunAnimation(10)
            PushbackX(-19800)
            AirPushbackX(-6000)
            AirPushbackY(-8000)
            AddX(250000)
            AddY(600000)
            physicsXImpulse(-10000)
            physicsYImpulse(-26000)
            SetAcceleration(-1000)
            setGravity(2600)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_37():
            AirHitstunAnimation(10)
            AirPushbackX(2000)
            AddX(-210000)
            AddY(0)
            physicsXImpulse(14000)
            physicsYImpulse(12000)
            SetAcceleration(1400)
            setGravity(-1200)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_38():
            AirHitstunAnimation(10)
            PushbackX(-19800)
            AirPushbackX(-8000)
            AirPushbackY(18000)
            AddX(280000)
            AddY(0)
            physicsXImpulse(-18000)
            physicsYImpulse(22000)
            SetAcceleration(-1800)
            setGravity(-2200)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)
        HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
    sprite('vrnyef_swdchain00', 1)
    AlphaValue(0)
    ConstantAlphaModifier(30)
    sprite('vrnyef_swdchain01', 1)
    sprite('vrnyef_swdchain02', 1)
    sprite('vrnyef_swdchain03', 1)
    sprite('vrnyef_swdchain04', 1)
    sprite('vrnyef_swdchain05', 1)
    sprite('vrnyef_swdchainatk', 6)
    RefreshMultihit()
    XImpulseAcceleration(180)
    YAccel(180)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    ObjectUpon(EVERY_FRAME, 32)
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')
    ObjectUpon(EVERY_FRAME, 32)


@State
def NY_SwordDChainOD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(4)
        Damage(300)
        AttackP1(80)
        Blockstun(24)
        AirUntechableTime(29)
        Hitstun(25)
        Hitstop(0)
        EnemyHitstopAddition(4, 4, 9)
        HitsparkSize(600)
        UseSlashHitspark(1)
        ChipPercentage(5)
        StarterRating(2)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CopyFromRightToLeft(23, 2, 83, 3, 2, 59)
        CopyFromRightToLeft(23, 2, 23, 3, 2, 60)
        CancelIfPlayerHit(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateParticle('nyef_breakA', 101)
        uponSendToLabel(LANDING, 1)

        def upon_32():
            PushbackX(19800)
            AirPushbackY(25000)
            AirPushbackX(-2000)
            AddX(-50000)
            AddY(600000)
            physicsXImpulse(10000)
            physicsYImpulse(-20000)
            SetAcceleration(1000)
            setGravity(2000)
            RotationSomething(0)

        def upon_33():
            AirHitstunAnimation(10)
            PushbackX(12000)
            AirPushbackX(-8000)
            AirPushbackY(30000)
            AddX(320000)
            AddY(0)
            physicsXImpulse(-10000)
            physicsYImpulse(14000)
            SetAcceleration(-1000)
            setGravity(-1400)
            RotationSomething(0)

        def upon_34():
            PushbackX(-19800)
            AirPushbackX(-8000)
            AddX(100000)
            AddY(50000)
            physicsXImpulse(-20000)
            physicsYImpulse(20000)
            SetAcceleration(-2000)
            setGravity(-2000)
            RotationSomething(0)

        def upon_35():
            AirPushbackX(3000)
            AirPushbackY(8000)
            AddX(-50000)
            AddY(600000)
            physicsXImpulse(10000)
            physicsYImpulse(-20000)
            SetAcceleration(2000)
            setGravity(4000)
            RotationSomething(0)

        def upon_36():
            AirUntechableTime(33)
            AirHitstunAnimation(10)
            PushbackX(-19800)
            AirPushbackX(-6000)
            AirPushbackY(-8000)
            AddX(450000)
            AddY(400000)
            physicsXImpulse(-24000)
            physicsYImpulse(-20000)
            SetAcceleration(-2400)
            setGravity(2000)
            RotationSomething(0)

        def upon_37():
            AirUntechableTime(33)
            AirHitstunAnimation(10)
            AirPushbackX(2000)
            AddX(-240000)
            AddY(120000)
            physicsXImpulse(24000)
            physicsYImpulse(10000)
            SetAcceleration(2400)
            setGravity(-1000)
            RotationSomething(0)

        def upon_38():
            AirUntechableTime(33)
            AirHitstunAnimation(10)
            PushbackX(-19800)
            AirPushbackX(-8000)
            AirPushbackY(18000)
            AddX(450000)
            AddY(50000)
            physicsXImpulse(-36000)
            physicsYImpulse(22000)
            SetAcceleration(-3600)
            setGravity(-2200)
            RotationSomething(0)
        HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
    sprite('vrnyef_swdchain00', 4)
    PushSpeedX()
    PushSpeedY()
    EndMomentum(1)
    AlphaValue(0)
    sprite('vrnyef_swdchain00', 1)
    PopSpeedX()
    PopSpeedY()
    ConstantAlphaModifier(30)
    CreateObject('NY_SummonA', -1)
    sprite('vrnyef_swdchain01', 1)
    sprite('vrnyef_swdchain02', 1)
    sprite('vrnyef_swdchain03', 1)
    sprite('vrnyef_swdchain04', 1)
    sprite('vrnyef_swdchain05', 1)
    sprite('vrnyef_swdchainatk', 10)
    XImpulseAcceleration(180)
    YAccel(180)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_BlackArea():

    def upon_IMMEDIATE():
        SetZVal(-500)
        AddX(160000)
    sprite('null', 120)
    CreateParticle('nyef_blackptcstart', -1)
    CreateParticle('nyef_sumlight00', -1)


@State
def NY_TripleSword11Mode():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        SLOT_51 = 200
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_32():
            ObjectUpon(FALLING, 41)
            ObjectUpon(5, 41)
            ObjectUpon(6, 41)
            ObjectUpon(CORNERED, 41)
            ObjectUpon(8, 41)
            sendToLabel(1)

        def upon_PLAYER_DAMAGED():
            ObjectUpon(FALLING, 41)
            ObjectUpon(5, 41)
            ObjectUpon(6, 41)
            ObjectUpon(CORNERED, 41)
            ObjectUpon(8, 41)
            sendToLabel(1)

        def upon_39():
            SLOT_51 = 11

        def upon_EVERY_FRAME():
            if SLOT_51:
                SLOT_51 = SLOT_51 + -1
                if not SLOT_51:
                    sendToLabel(1)
            if SLOT_XDistanceFromCenterOfStage > 2100000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
            if SLOT_XDistanceFromCenterOfStage < -2100000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
        if CharacterIDCheck('ta'):
            clearUponHandler(EVERY_FRAME)

            def upon_EVERY_FRAME():
                if SLOT_51:
                    SLOT_51 = SLOT_51 + -1
                    if not SLOT_51:
                        sendToLabel(1)
                if SLOT_XDistanceFromCenterOfStage > 3900000:
                    sendToLabel(1)
                    clearUponHandler(EVERY_FRAME)
                if SLOT_XDistanceFromCenterOfStage < -3900000:
                    sendToLabel(1)
                    clearUponHandler(EVERY_FRAME)
        AddX(100000)
        Size(1300)
    sprite('null', 1)
    CreateObject('NY_BlackArea', -1)
    sprite('null', 1)
    CancelIfPlayerHit(0)
    label(0)
    sprite('null', 8)
    AddX(180000)
    CreateParticle('nyef_blackptcstart', -1)
    RegisterObject(8, 7)
    RegisterObject(7, 6)
    RegisterObject(6, 5)
    RegisterObject(5, 4)
    CreateObject('NY_SwordD400_Attack11Mode', -1)
    RegisterObject(4, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)


@State
def NY_TripleSword13Mode():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        SLOT_51 = 200

        def upon_32():
            ObjectUpon(FALLING, 41)
            ObjectUpon(5, 41)
            ObjectUpon(6, 41)
            ObjectUpon(CORNERED, 41)
            ObjectUpon(8, 41)
            sendToLabel(1)
        SLOT_4 = 2

        def upon_37():
            SLOT_52 = 1

        def upon_38():
            SLOT_4 = 0
            SLOT_51 = 11
            Size(1200)

        def upon_39():
            SLOT_4 = 1
            SLOT_51 = 27

        def upon_40():
            SLOT_4 = 1
            SLOT_51 = 27

        def upon_41():
            SLOT_4 = 1
            SLOT_51 = 27

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_EVERY_FRAME():
            if SLOT_51:
                SLOT_51 = SLOT_51 + -1
                if not SLOT_51:
                    sendToLabel(1)
            if SLOT_XDistanceFromCenterOfStage > 2100000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
            if SLOT_XDistanceFromCenterOfStage < -2100000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
        if CharacterIDCheck('ta'):
            clearUponHandler(EVERY_FRAME)

            def upon_EVERY_FRAME():
                if SLOT_51:
                    SLOT_51 = SLOT_51 + -1
                    if not SLOT_51:
                        sendToLabel(1)
                if SLOT_XDistanceFromCenterOfStage > 3900000:
                    sendToLabel(1)
                    clearUponHandler(EVERY_FRAME)
                if SLOT_XDistanceFromCenterOfStage < -3900000:
                    sendToLabel(1)
                    clearUponHandler(EVERY_FRAME)
        AddX(70000)
    sprite('null', 1)
    CreateObject('NY_BlackArea', -1)
    sprite('null', 1)
    CancelIfPlayerHit(0)
    label(0)
    sprite('null', 8)
    SpriteIfNot0(6, 2, 52)
    AddX(180000)
    CreateParticle('nyef_blackptcstart', -1)
    RegisterObject(8, 7)
    RegisterObject(7, 6)
    RegisterObject(6, 5)
    RegisterObject(5, 4)
    if SLOT_4 == 2:
        CreateObject('NY_SwordD400_D', -1)
    if SLOT_4 == 1:
        CreateObject('NY_SwordD400', -1)
    if SLOT_4 == 0:
        CreateObject('NY_SwordD400_C', -1)
    RegisterObject(4, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)


@Subroutine
def NY_TripleSword_Init():
    AddX(70000)
    CancelIfPlayerHit(3)

    def upon_32():
        ObjectUpon(FALLING, 41)
        ObjectUpon(5, 41)
        ObjectUpon(6, 41)
        ObjectUpon(CORNERED, 41)
        ObjectUpon(8, 41)
        sendToLabel(1)
    SLOT_4 = 1

    def upon_STATE_END():
        SLOT_4 = 0
        SLOT_7 = 0

    def upon_EVERY_FRAME():
        if SLOT_51:
            SLOT_51 = SLOT_51 + -1
            if not SLOT_51:
                sendToLabel(1)
        if SLOT_XDistanceFromCenterOfStage > 2100000:
            sendToLabel(1)
            clearUponHandler(EVERY_FRAME)
        if SLOT_XDistanceFromCenterOfStage < -2100000:
            sendToLabel(1)
            clearUponHandler(EVERY_FRAME)
    if CharacterIDCheck('ta'):
        clearUponHandler(EVERY_FRAME)

        def upon_EVERY_FRAME():
            if SLOT_51:
                SLOT_51 = SLOT_51 + -1
                if not SLOT_51:
                    sendToLabel(1)
            if SLOT_XDistanceFromCenterOfStage > 3900000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
            if SLOT_XDistanceFromCenterOfStage < -3900000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)


@State
def NY_TripleSword():

    def upon_IMMEDIATE():
        SLOT_51 = 27
        if SLOT_7:
            SLOT_51 = 200
        callSubroutine('NY_TripleSword_Init')
    sprite('null', 1)
    CreateObject('NY_BlackArea', -1)
    sprite('null', 1)
    CancelIfPlayerHit(0)
    label(0)
    sprite('null', 8)
    AddX(180000)
    CreateParticle('nyef_blackptcstart', -1)
    RegisterObject(8, 7)
    RegisterObject(7, 6)
    RegisterObject(6, 5)
    RegisterObject(5, 4)
    CreateObject('NY_SwordD400', -1)
    RegisterObject(4, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)


@State
def NY_TripleSword_C():

    def upon_IMMEDIATE():
        SLOT_51 = 11
        Size(1200)
        if SLOT_7:
            SLOT_51 = 27
            Size(1000)
        callSubroutine('NY_TripleSword_Init')
    sprite('null', 1)
    CreateObject('NY_BlackArea', -1)
    sprite('null', 1)
    CancelIfPlayerHit(0)
    label(0)
    sprite('null', 8)
    AddX(180000)
    CreateParticle('nyef_blackptcstart', -1)
    RegisterObject(8, 7)
    RegisterObject(7, 6)
    RegisterObject(6, 5)
    RegisterObject(5, 4)
    CreateObject('NY_SwordD400_C', -1)
    RegisterObject(4, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)


@State
def NY_TripleSword_D():

    def upon_IMMEDIATE():
        SLOT_51 = 200
        if SLOT_7:
            SLOT_51 = 200
            SLOT_52 = 1
        callSubroutine('NY_TripleSword_Init')
    sprite('null', 1)
    CreateObject('NY_BlackArea', -1)
    sprite('null', 1)
    CancelIfPlayerHit(0)
    label(0)
    sprite('null', 8)
    SpriteIfNot0(6, 2, 52)
    AddX(180000)
    CreateParticle('nyef_blackptcstart', -1)
    RegisterObject(8, 7)
    RegisterObject(7, 6)
    RegisterObject(6, 5)
    RegisterObject(5, 4)
    CreateObject('NY_SwordD400_D', -1)
    RegisterObject(4, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)


@State
def NY_SwordD400():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(5)
        Damage(1200)
        AttackP1(80)
        SingleProration(1)
        SameMoveProration(10)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(48)
        AirPushbackY(38000)
        Hitstop(0)
        EnemyHitstopAddition(15, 15, 15)
        UseSlashHitspark(1)
        VoodooDamageMultiplier(2)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)

        def upon_54():
            ObjectUpon(LANDING, 32)

        def upon_41():
            EndAttack()
        E0EAEffectScale(2)
        PaletteIndex(1)
        RotationAngle(-90000)
        EnableAfterimage(1)
        AfterimageInterval(2)
        AfterimageCount(3)
        AfterimageColor_1(128, 255, 0, 0)
        AfterimageColor_2(255, 255, 0, 0)
        AfterimageSize_1(1050)
        AfterimageSize_2(1100)
    sprite('vrnyef_swd400atk00', 12)
    AlphaValue(240)
    setGravity(-800)
    SetScaleX(520)
    SetScaleXPerFrame(40)
    CreateObject('NY_SwordD400_effA', -1)
    CreateObject('NY_SwordD400_effB', -1)
    AddY(-104000)
    PrivateSE('nyse_32')
    sprite('vrnyef_swd400atk01', 1)
    setGravity(-8000)
    AddY(42000)
    SetScaleSpeed(0)
    Size(1000)
    sprite('vrnyef_swd400atk02', 1)
    sprite('vrnyef_swd400atk03', 1)
    sprite('vrnyef_swd400atk', 6)
    setGravity(-6000)
    physicsYImpulse(24000)
    sprite('vrnyef_swd400atk', 10)
    setGravity(0)
    physicsYImpulse(16000)
    SetScaleXPerFrame(-10)
    SetScaleSpeedY(-100)
    AlphaValue(120)
    ConstantAlphaModifier(-12)
    EndAttack()
    CreateObject('NY_MagicA', -1)
    CreateObject('DIST_TriSwd', -1)
    CreateParticle('nyef_blackptcdel', -1)


@State
def NY_SwordD400_C():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(5)
        Damage(1000)
        AttackP1(80)
        SingleProration(1)
        SameMoveProration(10)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(48)
        AirPushbackY(33000)
        AirPushbackX(3000)
        Hitstop(0)
        EnemyHitstopAddition(15, 15, 15)
        UseSlashHitspark(1)
        ProjectileLevel(2)
        VoodooDamageMultiplier(2)
        ScreenShake(2000, 6000)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)

        def upon_54():
            ObjectUpon(LANDING, 32)

        def upon_41():
            EndAttack()
        E0EAEffectScale(2)
        PaletteIndex(1)
        RotationAngle(-90000)
        EnableAfterimage(1)
        AfterimageInterval(2)
        AfterimageCount(3)
        AfterimageColor_1(128, 255, 0, 0)
        AfterimageColor_2(255, 255, 0, 0)
        AfterimageSize_1(1050)
        AfterimageSize_2(1100)
    sprite('vrnyef_swd400atk00', 12)
    AlphaValue(240)
    setGravity(-800)
    SetScaleX(520)
    SetScaleXPerFrame(40)
    CreateObject('NY_SwordD400_effA', -1)
    CreateObject('NY_SwordD400_effB', -1)
    AddY(-104000)
    PrivateSE('nyse_32')
    sprite('vrnyef_swd400atk01', 1)
    setGravity(-8000)
    AddY(42000)
    SetScaleSpeed(0)
    Size(1000)
    sprite('vrnyef_swd400atk02', 1)
    sprite('vrnyef_swd400atk03', 1)
    sprite('vrnyef_swd400atk', 6)
    setGravity(-6000)
    physicsYImpulse(24000)
    sprite('vrnyef_swd400atk', 10)
    setGravity(0)
    physicsYImpulse(16000)
    SetScaleXPerFrame(-10)
    SetScaleSpeedY(-100)
    AlphaValue(120)
    ConstantAlphaModifier(-12)
    EndAttack()
    CreateObject('NY_MagicA', -1)
    CreateObject('DIST_TriSwd', -1)
    CreateParticle('nyef_blackptcdel', -1)


@State
def NY_SwordD400_D():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(5)
        Damage(1500)
        AttackP1(80)
        SingleProration(1)
        SameMoveProration(10)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(48)
        AirPushbackY(38000)
        Hitstop(0)
        EnemyHitstopAddition(15, 15, 15)
        UseSlashHitspark(1)
        VoodooDamageMultiplier(2)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)

        def upon_54():
            ObjectUpon(LANDING, 32)

        def upon_41():
            EndAttack()
        E0EAEffectScale(2)
        PaletteIndex(1)
        RotationAngle(-90000)
        EnableAfterimage(1)
        AfterimageInterval(2)
        AfterimageCount(3)
        AfterimageColor_1(128, 255, 0, 0)
        AfterimageColor_2(255, 255, 0, 0)
        AfterimageSize_1(1050)
        AfterimageSize_2(1100)
    sprite('vrnyef_swd400atk00', 12)
    AlphaValue(240)
    setGravity(-800)
    SetScaleX(520)
    SetScaleXPerFrame(40)
    CreateObject('NY_SwordD400_effA', -1)
    CreateObject('NY_SwordD400_effB', -1)
    AddY(-104000)
    PrivateSE('nyse_32')
    sprite('vrnyef_swd400atk01', 1)
    setGravity(-8000)
    AddY(42000)
    SetScaleSpeed(0)
    Size(1000)
    sprite('vrnyef_swd400atk02', 1)
    sprite('vrnyef_swd400atk03', 1)
    sprite('vrnyef_swd400atk', 6)
    setGravity(-6000)
    physicsYImpulse(24000)
    sprite('vrnyef_swd400atk', 10)
    setGravity(0)
    physicsYImpulse(16000)
    SetScaleXPerFrame(-10)
    SetScaleSpeedY(-100)
    AlphaValue(120)
    ConstantAlphaModifier(-12)
    EndAttack()
    CreateObject('NY_MagicA', -1)
    CreateObject('DIST_TriSwd', -1)
    CreateParticle('nyef_blackptcdel', -1)


@State
def NY_SwordD400_effA():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(-100)
        AddX(-30000)
        RotationAngle(-65000)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(6)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('null', 2)
    sprite('vrnyef_swd400a', 8)
    AlphaValue(80)
    ConstantAlphaModifier(20)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    sprite('vrnyef_swd400a', 12)
    ConstantAlphaModifier(-24)


@State
def NY_SwordD400_effB():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(-100)
        AddX(60000)
        RotationAngle(245000)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(6)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('null', 2)
    sprite('vrnyef_swd400a', 8)
    AlphaValue(80)
    ConstantAlphaModifier(20)
    physicsXImpulse(-5000)
    physicsYImpulse(15000)
    sprite('vrnyef_swd400a', 12)
    ConstantAlphaModifier(-20)


@State
def NY_SwordD400_Attack11Mode():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        AttackP2(80)
        SameMoveProration(10)
        UseSlashHitspark(1)
        EnemyHitstopAddition(15, 15, 15)

        def upon_OPPONENT_HIT_OR_BLOCK():
            ObjectUpon(LANDING, 32)
        E0EAEffectScale(2)
        Damage(900)
        Hitstop(6)
        AirPushbackX(5000)
        AirPushbackY(35000)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirUntechableTime(50)
        Blockstun(19)

        def upon_41():
            EndAttack()
        PaletteIndex(1)
        RotationAngle(-90000)
        EnableAfterimage(1)
        AfterimageInterval(2)
        AfterimageCount(3)
        AfterimageColor_1(128, 255, 0, 0)
        AfterimageColor_2(255, 255, 0, 0)
        AfterimageSize_1(1050)
        AfterimageSize_2(1100)
    sprite('vrnyef_swd400atk00', 12)
    AlphaValue(240)
    setGravity(-800)
    SetScaleX(520)
    SetScaleXPerFrame(40)
    CreateObject('NY_SwordD400_effA', -1)
    CreateObject('NY_SwordD400_effB', -1)
    AddY(-104000)
    sprite('vrnyef_swd400atk01', 1)
    setGravity(-8000)
    AddY(42000)
    SetScaleSpeed(0)
    Size(1000)
    sprite('vrnyef_swd400atk02', 1)
    sprite('vrnyef_swd400atk03', 1)
    sprite('vrnyef_swd400atk', 6)
    setGravity(-6000)
    physicsYImpulse(24000)
    sprite('vrnyef_swd400atk', 10)
    setGravity(0)
    physicsYImpulse(16000)
    SetScaleXPerFrame(-10)
    SetScaleSpeedY(-100)
    AlphaValue(120)
    ConstantAlphaModifier(-12)
    EndAttack()
    CreateObject('NY_MagicA', -1)
    CreateObject('DIST_TriSwd', -1)
    CreateParticle('nyef_blackptcdel', -1)


@State
def White():
    sprite('vr_white', 30)
    SetZVal(-500)
    BlendMode_Normal()
    AlphaValue(0)
    ConstantAlphaModifier(20)
    ScreenPosition(1)
    SetPosXByScreenPer(50)
    SetPosYByScreenPer(-50)
    AbsoluteY(-450000)
    XPositionRelativeFacingAbsolute(640000)
    Size(4000)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-10)


@State
def StartWhite():
    sprite('vr_white', 40)
    SetZVal(-500)
    BlendMode_Normal()
    AlphaValue(0)
    ConstantAlphaModifier(20)
    ScreenPosition(1)
    SetPosXByScreenPer(50)
    SetPosYByScreenPer(-50)
    AbsoluteY(-450000)
    XPositionRelativeFacingAbsolute(640000)
    Size(4000)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-10)


@State
def FinishWhite():
    sprite('vr_white', 30)
    SetZVal(-500)
    BlendMode_Normal()
    AlphaValue(255)
    ScreenPosition(1)
    SetPosXByScreenPer(50)
    SetPosYByScreenPer(-50)
    AbsoluteY(-450000)
    XPositionRelativeFacingAbsolute(640000)
    Size(4000)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-10)


@State
def NY_AHAnime():

    def upon_IMMEDIATE():
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(-450000)
        XPositionRelativeFacingAbsolute(640000)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageMask_1(0, 255, 0, 0)
        AfterimageMask_2(0, 0, 0, 0)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
        FaceRight()
    sprite('null', 40)
    sprite('ny450_a00', 4)
    Size(900)
    SetScaleSpeed(1)
    setGravity(-2)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    Voiceline('ny292')
    if SLOT_43:
        Mouth(13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665,
            13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 
            13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 
            13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 
            13665, 13667, 13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Mouth(13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665,
            13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 
            13665, 13923, 24880, 25397, 24885, 25397, 24885, 25397, 24885, 
            25397, 24885, 25397, 24885, 25397, 24885, 25397, 24885, 25397, 
            24885, 25397, 24885, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    CreateObject('Astral3DFunnel', -1)
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_1')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a04', 7)
    Size(1000)
    SetScaleSpeed(0)
    setGravity(1)
    sprite('ny450_a05', 7)
    sprite('ny450_a06', 7)
    sprite('ny450_a07', 7)
    CommonSE('019_quake_0')
    sprite('ny450_a08', 7)
    sprite('ny450_a09', 5)
    CommonSE('019_quake_1')
    sprite('ny450_a10', 5)
    sprite('ny450_a11', 5)
    sprite('ny450_a12', 5)
    sprite('ny450_a13', 5)
    sprite('ny450_a14', 5)
    sprite('ny450_a15', 5)
    sprite('ny450_a16', 5)
    PrivateSE('nyse_27')
    sprite('ny450_a17', 6)
    sprite('ny450_a19', 6)
    PrivateSE('nyse_27')
    sprite('ny450_a20', 6)
    sprite('ny450_a21', 6)
    PrivateSE('nyse_27')
    sprite('ny450_a22', 4)
    setGravity(0)
    PrivateSE('nyse_27')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    sprite('ny450_a23', 4)
    PrivateSE('nyse_27')
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    PrivateSE('nyse_27')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    PrivateSE('nyse_27')
    sprite('ny450_a22', 4)
    sprite('ny450_a23', 4)
    setGravity(-1)
    YAccel(80)
    sprite('ny450_a24', 4)
    YAccel(80)
    sprite('ny450_a22', 4)
    YAccel(80)
    sprite('ny450_a23', 4)
    YAccel(80)
    sprite('ny450_a24', 4)
    YAccel(80)
    sprite('ny450_a22', 4)
    YAccel(80)
    sprite('ny450_a23', 4)
    YAccel(80)
    sprite('ny450_a24', 4)
    YAccel(0)
    sprite('ny450_a22', 4)
    PrivateSE('nyse_04')
    CommonSE('019_quake_1')
    PrivateSE('nyse_28')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    PrivateSE('nyse_04')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    PrivateSE('nyse_04')
    CommonSE('019_quake_0')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    CommonSE('019_quake_0')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    CommonSE('019_quake_0')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    setGravity(0)
    sprite('ny450_a25', 5)
    physicsYImpulse(0)
    setGravity(0)
    Voiceline('ny293')
    CommonSE('011_spin_0')
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a23', 4)
    CommonSE('011_spin_0')
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a26', 4)
    sprite('ny450_a27', 4)
    sprite('ny450_a28', 4)
    sprite('ny450_a29', 4)
    sprite('ny450_a30', 4)
    ConstantAlphaModifier(-10)
    sprite('ny450_a31', 30)


@State
def Astral3DFunnel():

    def upon_IMMEDIATE():
        SetZVal(-1000)
        BlendMode_Add()
        ScreenPosition(1)
        SetPosYByScreenPer(-50)
        SetPosXByScreenPer(50)
        AddY(-1600000)
    sprite('null', 180)
    Eff3DEffect('nyah_funnel.DIG', 'nyah_funnel_mt_000.mmot')
    AlphaValue(0)
    ConstantAlphaModifier(10)
    SetScaleSpeed(1)
    Size(1400)
    sprite('null', 7)
    AddY(-15000)
    AddScale(100)
    physicsYImpulse(-2500)
    sprite('null', 7)
    AddY(-15000)
    AddScale(50)
    sprite('null', 7)
    AddScale(100)
    sprite('null', 7)
    sprite('null', 7)
    sprite('null', 5)
    sprite('null', 60)
    SetScaleSpeed(50)
    physicsYImpulse(-40000)


@State
def AstrakFinishPtc():

    def upon_IMMEDIATE():
        LinkParticle('nyef_ashfinish')
        Flip()
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(0)
    sprite('null', 32767)


@State
def AstralSword():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        DefeatOpponentBehavior(3)
        Hitstop(30)
        AttackDirection(3)
        uponSendToLabel(LANDING, 0)
        Flip()
        AbsoluteY(2000000)
        AddX(1600000)
        Size(3000)
    sprite('vr_sword', 32767)
    physicsXImpulse(-100000)
    physicsYImpulse(-100000)
    label(0)
    sprite('vr_sword', 130)
    HitAnywhere(1)
    EndMomentum(1)
    ScreenShake(200000, 0)
    sprite('vr_sword', 20)
    PrivateSE('nyse_04')
    BlendMode_Normal()
    ConstantAlphaModifier(-30)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 0)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 1)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 2)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 3)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 4)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 5)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 6)


@State
def AstralLookAtMeDummy():
    sprite('null', 2000)
    CameraControlEnable(1)
    CameraFast(1)
    TeleportToObject(22)
    AbsoluteY(0)
    RemoveOnCallStateEnd(3)


@State
def NY_AirCurveSword13Mode():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        AlphaValue(255)
        RotationAngle(-10000)
        EnableAfterimage(1)
        AfterimageBlendMode(1)
        AfterimageCount(6)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        Damage(1000)
        AttackP1(80)
        SameMoveProration(10)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(20000)
        AirPushbackY(-50000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(40)
        HardKnockdown(1)
        HitOverhead(2)
        UseSlashHitspark(1)
        CHGroundBounce(1)
        CHAirPushbackX(6000)
        BouncePercentage(50)
        StarterRating(2)
        AddX(160000)
        AddY(380000)

        def upon_34():
            Size(1200)
            AddX(-60000)
            Damage(1100)
            AirUntechableTime(70)
            GroundBounce(1)
            AirPushbackX(6000)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrnyef_swdg00', 6)
    Visibility(1)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg00', 1)
    Visibility(0)
    AddScale(-280)
    SetScaleSpeed(10)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    PrivateSE('nyse_28')
    sprite('vrnyef_swdg01', 1)
    sprite('vrnyef_swdg01', 1)
    sprite('vrnyef_swdg01', 1)
    AddScale(20)
    AddRotationPerFrame(3000)
    SetAcceleration(300)
    SetScaleSpeed(50)
    StartMultihit()
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg01', 1)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg02', 1)
    CreateParticle('nyef_sumB', 5)
    PrivateSE('nyse_33')
    sprite('vrnyef_swdg03', 1)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg04', 4)
    SetScaleSpeed(0)
    AddRotationPerFrame(500)
    ConstantAlphaModifier(-5)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg05', 4)
    AlphaValue(200)
    ConstantAlphaModifier(-50)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    CreateParticle('nyef_sumBlight', 5)


@State
def NY_AirCurveSword_D():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        AlphaValue(255)
        RotationAngle(-10000)
        EnableAfterimage(1)
        AfterimageBlendMode(1)
        AfterimageCount(6)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        Damage(1200)
        AttackP1(80)
        SameMoveProration(10)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(20000)
        AirPushbackY(-50000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(40)
        HardKnockdown(1)
        HitOverhead(2)
        UseSlashHitspark(1)
        CHGroundBounce(1)
        CHAirPushbackX(6000)
        BouncePercentage(50)
        StarterRating(2)
        AddX(160000)
        AddY(380000)

        def upon_33():
            Size(1200)
            AddX(-60000)
            Damage(1320)
            AirUntechableTime(70)
            GroundBounce(1)
            AirPushbackX(6000)
    sprite('vrnyef_swdg00', 6)
    Visibility(1)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg00', 1)
    Visibility(0)
    AddScale(-280)
    SetScaleSpeed(10)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg01', 1)
    sprite('vrnyef_swdg01', 1)
    sprite('vrnyef_swdg01', 1)
    AddScale(20)
    AddRotationPerFrame(3000)
    SetAcceleration(300)
    SetScaleSpeed(50)
    StartMultihit()
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg01', 1)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg02', 1)
    CreateParticle('nyef_sumB', 5)
    PrivateSE('nyse_33')
    sprite('vrnyef_swdg03', 1)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg04', 4)
    SetScaleSpeed(0)
    AddRotationPerFrame(500)
    ConstantAlphaModifier(-5)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg05', 4)
    AlphaValue(200)
    ConstantAlphaModifier(-50)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    CreateParticle('nyef_sumBlight', 5)


@State
def NY_AirCurveSword11Mode():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        AlphaValue(255)
        RotationAngle(-10000)
        EnableAfterimage(1)
        AfterimageBlendMode(1)
        AfterimageCount(6)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        Damage(1000)
        SameMoveProration(85)
        UseSlashHitspark(1)
        CHAirUntechableTime(40)
        AddX(135000)
        AddY(450000)
        Size(1330)
        AttackP1(80)
        HitOverhead(2)
        GroundedHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(-30000)
        AirUntechableTime(40)
        GroundBounce(1)
        BouncePercentage(45)
        CHBouncePercentage(60)
    sprite('vrnyef_swdg00', 2)
    AddScale(-280)
    SetScaleSpeed(10)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    PrivateSE('nyse_28')
    sprite('vrnyef_swdg01', 2)
    sprite('vrnyef_swdg01', 2)
    sprite('vrnyef_swdg01', 1)
    AddScale(20)
    AddRotationPerFrame(5000)
    SetAcceleration(300)
    SetScaleSpeed(50)
    StartMultihit()
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg01', 1)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg02', 1)
    CreateParticle('nyef_sumB', 5)
    PrivateSE('nyse_33')
    sprite('vrnyef_swdg03', 1)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg04', 4)
    SetScaleSpeed(0)
    AddRotationPerFrame(500)
    ConstantAlphaModifier(-5)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg05', 4)
    AlphaValue(200)
    ConstantAlphaModifier(-50)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    CreateParticle('nyef_sumBlight', 5)


@State
def BottomSword11Mode():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        PaletteIndex(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(4)
        AfterimageCount(4)
        AfterimageColor_1(200, 90, 90, 90)
        AfterimageColor_2(140, 90, 90, 90)
        AfterimageMask_1(0, 0, 160, 255)
        AfterimageMask_2(0, 100, 180, 40)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        Damage(250)
        AirHitstunAnimation(9)
        AirPushbackY(5000)
        AirUntechableTime(30)
        AttackP1(80)
        SingleProration(1)
        SameMoveProration(10)
        UseSlashHitspark(1)
        Hitstop(4)
        PushbackX(12000)
        ChipPercentage(20)
        AddY(-32000)
        physicsXImpulse(6000)
        ContinueState(120)
        Unknown12052(2)

        def upon_32():
            if SLOT_19 < 650000:
                CopyFromRightToLeft(23, 2, 83, 22, 2, 83)
            else:
                AddX(550000)

        def upon_33():
            AddX(900000)
            Flip()
            XImpulseAcceleration(-100)

        def upon_OPPONENT_HIT_OR_BLOCK():
            WallCollisionDetection(1)
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if SLOT_2 > 3:
                AirPushbackY(-10000)
                AirUntechableTime(40)
                HardKnockdown(1)
            if SLOT_2 > 4:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(580)
        HitsPerCall(1, 0, 0, 0, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
    sprite('null', 1)
    CommonSE('022_magiccircle_b')
    sprite('vrnyef_swdf03', 8)
    PushSpeedX()
    EndMomentum(1)
    AttackOff()
    Visibility(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    sprite('vrnyef_swdf03', 8)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    sprite('null', 1)
    Visibility(0)
    PopSpeedX()
    label(0)
    sprite('vrnyef_swdf00', 1)
    CommonSE('006_swing_blade_2')
    AttackOff()
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    RefreshMultihit()
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    sprite('vrnyef_swdf04', 1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 1)
    sprite('vrnyef_swdf06', 1)
    sprite('vrnyef_swdf07', 1)
    AttackOff()
    AddActionMark(1)
    gotoLabel(0)
    label(580)
    sprite('keep', 30)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-20)


@State
def BottomSword():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        AddX(200000)
        AddY(-32000)
        AlphaValue(0)
        ConstantAlphaModifier(30)
        RotationAngle(-90000)
        AddRotationPerFrame(10000)
        ContinueState(120)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageColor_1(128, 255, 255, 255)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        SameMoveProration(1)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        CHAirHitstunAnimation(17)
        CHGroundedHitstunAnimation(17)
        AirPushbackX(25000)
        AirPushbackY(18000)
        AirUntechableTime(40)
        Wallbounce(1)
        NonCornerWallbounce(1)
        WallbounceReboundTime(10)
        CHFloorslide(10)
        UseSlashHitspark(1)
        AttackDirection(0)
        StarterRating(2)
        physicsXImpulse(40000)

        def upon_45():
            if SLOT_StateDuration > 70:
                CollideWithWall(1)
        HitsPerCall(1, 0, 1, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
        ContinueState(60)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrnyef_swdf03', 3)
    WallCollisionDetection(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CommonSE('022_magiccircle_b')
    sprite('vrnyef_swdf03', 3)
    WallCollisionDetection(0)
    sprite('vrnyef_swdf03', 3)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    label(3)
    sprite('vrnyef_swdf04', 1)
    CommonSE('006_swing_blade_2')
    RotationAngle(0)
    AddRotationPerFrame(0)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 2)
    sprite('vrnyef_swdf06', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf07', 2)
    sprite('vrnyef_swdf08', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf09', 2)
    sprite('vrnyef_swdf00', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    loopRest()
    gotoLabel(3)
    label(580)
    sprite('keep', 30)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    XImpulseAcceleration(20)
    physicsYImpulse(0)
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-20)
    AttackOff()


@State
def BottomSword_C():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        AddX(200000)
        AddY(-32000)
        AlphaValue(0)
        ConstantAlphaModifier(30)
        RotationAngle(-90000)
        AddRotationPerFrame(10000)
        ContinueState(120)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageColor_1(128, 255, 255, 255)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        SameMoveProration(1)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(2)
        CHAirHitstunAnimation(17)
        CHGroundedHitstunAnimation(2)
        Stagger(49)
        Crumple(39)
        PushbackX(-39900)
        AirPushbackX(-44000)
        AirPushbackY(2000)
        AirUntechableTime(40)
        Wallbounce(1)
        WallbounceReboundTime(10)
        Floorslide(10)
        UseSlashHitspark(1)
        AttackDirection(0)
        FlipOnHit(1)
        StarterRating(2)
        AddX(820000)
        Flip()
        physicsXImpulse(25000)

        def upon_45():
            if SLOT_StateDuration > 70:
                CollideWithWall(1)
        HitsPerCall(1, 0, 1, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
        ContinueState(60)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('vrnyef_swdf03', 6)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CommonSE('022_magiccircle_b')
    sprite('vrnyef_swdf03', 3)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    label(3)
    sprite('vrnyef_swdf04', 1)
    CommonSE('006_swing_blade_2')
    RotationAngle(0)
    AddRotationPerFrame(0)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 2)
    sprite('vrnyef_swdf06', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf07', 2)
    sprite('vrnyef_swdf08', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf09', 2)
    sprite('vrnyef_swdf00', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    loopRest()
    gotoLabel(3)
    label(580)
    sprite('keep', 30)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    XImpulseAcceleration(20)
    physicsYImpulse(0)
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-20)
    AttackOff()


@State
def BottomSword_D():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        AddX(200000)
        AddY(-32000)
        AlphaValue(0)
        ConstantAlphaModifier(30)
        RotationAngle(-90000)
        AddRotationPerFrame(10000)
        ContinueState(120)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageColor_1(128, 255, 255, 255)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(4)
        Damage(980)
        AttackP1(80)
        SameMoveProration(1)
        HitLow(2)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackX(36000)
        AirPushbackY(10000)
        AirUntechableTime(48)
        Wallbounce(1)
        WallbounceReboundTime(10)
        Floorslide(10)
        FatalCounter(1)
        UseSlashHitspark(1)
        AttackDirection(0)
        StarterRating(2)
        physicsXImpulse(3000)
        AttackOff()
        AfterimageSize_1(1100)
        AfterimageSize_2(1200)

        def upon_45():
            if SLOT_StateDuration > 70:
                CollideWithWall(1)
        HitsPerCall(1, 0, 1, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
        ContinueState(60)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('vrnyef_swdf03', 3)
    WallCollisionDetection(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CommonSE('022_magiccircle_b')
    sprite('vrnyef_swdf03', 3)
    WallCollisionDetection(0)
    sprite('vrnyef_swdf03', 3)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf04', 1)
    RefreshMultihit()
    XImpulseAcceleration(2000)
    CommonSE('006_swing_blade_2')
    RotationAngle(0)
    AddRotationPerFrame(0)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    label(3)
    sprite('vrnyef_swdf05', 2)
    sprite('vrnyef_swdf06', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf07', 2)
    sprite('vrnyef_swdf08', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf09', 2)
    sprite('vrnyef_swdf00', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    sprite('vrnyef_swdf04', 1)
    CommonSE('006_swing_blade_2')
    RotationAngle(0)
    AddRotationPerFrame(0)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    loopRest()
    gotoLabel(3)
    label(580)
    sprite('keep', 30)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    XImpulseAcceleration(20)
    physicsYImpulse(0)
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-20)
    AttackOff()


@State
def SummonBottomSwordHold():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        PaletteIndex(1)
        SetPosXByScreenPer(105)
        AddY(-64000)
        SetScaleX(-1000)
        AlphaValue(0)
        ContinueState(120)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageColor_1(128, 255, 255, 255)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1100)
        AfterimageSize_2(1200)
        AttackLevel_(3)
        Damage(900)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(28)
        AirPushbackX(-3000)
        PushbackX(-18000)
        CollideWithWall(1)
        HitsPerCall(1, 0, 1, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
    sprite('vrnyef_swdf03', 6)
    RotationAngle(-90000)
    AddRotationPerFrame(-10000)
    physicsXImpulse(-30000)
    ConstantAlphaModifier(30)
    StartMultihit()
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    sprite('vrnyef_swdf03', 3)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    label(0)
    sprite('vrnyef_swdf04', 1)
    RotationAngle(0)
    AddRotationPerFrame(0)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 2)
    sprite('vrnyef_swdf06', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf07', 2)
    sprite('vrnyef_swdf08', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf09', 2)
    sprite('vrnyef_swdf00', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    loopRest()
    gotoLabel(0)
    label(580)
    sprite('keep', 30)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-20)


@State
def SummonDDBigSwordBoss():
    sprite('null', 20)
    IgnoreScreenfreeze(1)
    CreateObject('SummonDDBigSword', -1)
    AddX(150000)
    sprite('null', 20)
    CreateObject('SummonDDBigSword', -1)
    AddX(150000)
    sprite('null', 20)
    CreateObject('SummonDDBigSword', -1)
    AddX(150000)
    sprite('null', 20)
    CreateObject('SummonDDBigSword', -1)
    AddX(150000)


@State
def SummonDDBigSwordOverDrive():
    sprite('null', 15)
    IgnoreScreenfreeze(1)
    CreateObject('SummonDDBigSwordOD', -1)
    AddX(150000)
    sprite('null', 15)
    CreateObject('SummonDDBigSwordOD', -1)
    AddX(150000)
    sprite('null', 15)
    CreateObject('SummonDDBigSwordOD', -1)
    AddX(150000)
    sprite('null', 15)
    CreateObject('SummonDDBigSwordOD', -1)
    ObjectUpon(STATE_END, 32)
    AddX(150000)


@State
def SummonDDBigSword():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        AddX(406000)
        AddY(640000)
        SetZVal(-1)
        AlphaValue(0)
        WallCollisionDetection(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageColor_1(0, 255, 0, 0)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1030)
        AfterimageSize_2(1040)
        AttackLevel_(4)
        Damage(2400)
        MinimumDamage(40)
        AttackP1(70)
        AttackP2(82)
        GroundedHitstunAnimation(9)
        AirPushbackY(-100000)
        AirUntechableTime(100)
        HardKnockdown(1)
        YImpulseBeforeWallbounce(0)
        UseSlashHitspark(1)
        StarterRating(2)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 36)
        if SLOT_51:
            AddX(-150000)
        else:
            HitAirUnblockable(3)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrnyef_ddbigswd00', 41)
    CreateObject('NY_SumBigSword', -1)
    CreateObject('SummonDDBigSwordSub', -1)
    ConstantAlphaModifier(10)
    AddY(512000)
    physicsYImpulse(-1000)
    CreateParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd01', 1)
    AddY(-200000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    ScreenShake(0, 30000)
    PrivateSE('nyse_04')
    sprite('vrnyef_ddbigswd02', 1)
    AddY(-150000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd03', 1)
    AddY(-50000)
    CreateParticle('nyef_sumDDshock', 104)
    CreateParticle('nyef_sumDDshocklight00', 0)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd04', 8)
    AlphaValue(255)
    SetScaleSpeed(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    sprite('vrnyef_ddbigswd05', 25)
    physicsYImpulse(2000)
    ConstantAlphaModifier(-10)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)


@State
def SummonDDBigSwordOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        AddX(256000)
        AddY(640000)
        SetZVal(-1)
        AlphaValue(0)
        WallCollisionDetection(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageColor_1(0, 255, 0, 0)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1030)
        AfterimageSize_2(1040)
        AttackLevel_(4)
        Damage(1400)
        MinimumDamage(23)
        AttackP1(70)
        AttackP2(82)
        SingleProration(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(12500)
        AirPushbackY(11000)
        AirUntechableTime(100)
        Hitstop(1)
        EnemyHitstopAddition(0, 0, 0)
        UseSlashHitspark(1)
        HitAirUnblockable(3)
        StarterRating(2)
        VoodooDamageMultiplier(2)
        AttackType(4)
        CHStateIfCHStart(3)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 36)
        if SLOT_51:
            AddX(70000)
            HitAirUnblockable(0)

        def upon_32():
            AirPushbackY(-60000)
            HardKnockdown(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrnyef_ddbigswd00', 41)
    CreateObject('NY_SumBigSword', -1)
    CreateObject('SummonDDBigSwordSub', -1)
    ConstantAlphaModifier(10)
    AddY(512000)
    physicsYImpulse(-1000)
    CreateParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd01', 1)
    AddY(-200000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    ScreenShake(0, 30000)
    PrivateSE('nyse_04')
    sprite('vrnyef_ddbigswd02', 1)
    AddY(-150000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd03', 1)
    AddY(-50000)
    CreateParticle('nyef_sumDDshock', 104)
    CreateParticle('nyef_sumDDshocklight00', 0)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd04', 8)
    AlphaValue(255)
    SetScaleSpeed(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    sprite('vrnyef_ddbigswd05', 25)
    physicsYImpulse(2000)
    ConstantAlphaModifier(-10)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)


@State
def SummonDDBigSwordSub():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(1)
        SetZVal(-5)
        ContinueState(120)
        AlphaValue(0)
        WallCollisionDetection(1)
        EnableAfterimage(0)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(5)
        AfterimageColor_1(0, 255, 0, 0)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1020)
        AfterimageSize_2(1050)
    sprite('vrnyef_ddbigswdb00', 41)
    AddY(512000)
    physicsYImpulse(-500)
    ConstantAlphaModifier(20)
    sprite('vrnyef_ddbigswdb01', 1)
    AddY(-200000)
    sprite('vrnyef_ddbigswdb02', 1)
    AddY(-150000)
    sprite('vrnyef_ddbigswdb03', 1)
    AddY(-50000)
    sprite('vrnyef_ddbigswdb04', 8)
    physicsYImpulse(-500)
    AlphaValue(255)
    sprite('vrnyef_ddbigswdb05', 10)
    sprite('vrnyef_ddbigswdb05', 15)
    ConstantAlphaModifier(-20)


@State
def __6CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteIndex(1)
        PaletteEffType(1)
        PaletteColor1(14)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
    sprite('vrnyef213_f00', 8)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('vrnyef213_f00', 8)


@State
def __2CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteEffType(1)
        PaletteColor1(10)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
    sprite('vrnyef232_f00', 6)
    AlphaValue(0)
    ConstantAlphaModifier(40)
    sprite('vrnyef232_f01', 6)
    ConstantAlphaModifier(-40)


@State
def __8CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteEffType(1)
        PaletteColor1(12)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
    sprite('vrnyef252_f00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('vrnyef252_f01', 2)
    AlphaValue(255)
    ConstantAlphaModifier(-40)
    sprite('vrnyef252_f02', 4)


@State
def __82CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteEffType(1)
        PaletteColor1(10)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
    sprite('vrnyef254_f00', 2)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('vrnyef254_f01', 2)
    AlphaValue(255)
    ConstantAlphaModifier(-40)
    sprite('vrnyef254_f02', 2)


@State
def __3CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteEffType(1)
        PaletteColor1(12)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
    sprite('vrnyef234_f00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(40)
    SetScaleSpeedY(-5)
    sprite('vrnyef234_f00', 5)
    SetScaleSpeed(-5)
    ConstantAlphaModifier(-20)


@State
def Funnel2C():
    sprite('ny232_fx00', 2)
    sprite('ny232_fx01', 2)
    IgnorePauses(3)
    RemoveOnCallStateEnd(3)
    E0EAEffectPosition(3)
    sprite('ny232_fx02', 2)
    sprite('ny232_fx03', 2)
    sprite('ny232_fx04', 2)
    sprite('ny232_fx05', 2)
    sprite('ny232_fx06', 2)


@Subroutine
def Funnel5CReset():
    IgnorePauses(3)
    E0EAEffectPosition(3)
    RemoveOnCallStateEnd(3)
    AddY(300000)
    AddX(-100000)
    E0EAEffectObjectZ(3)
    SetZVal(1)
    PaletteIndex(0)


@State
def FunnelRevive():

    def upon_IMMEDIATE():
        callSubroutine('Funnel5CReset')
    sprite('ny202_f19', 2)
    sprite('ny202_f20', 2)
    sprite('ny202_f21', 2)
    sprite('ny202_f22', 32767)


@State
def Funnel5CMain():

    def upon_IMMEDIATE():
        callSubroutine('Funnel5CReset')
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        uponSendToLabel(36, 4)
        uponSendToLabel(37, 5)
        uponSendToLabel(38, 6)
        uponSendToLabel(39, 7)
        uponSendToLabel(40, 8)

        def upon_41():
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(35)
            clearUponHandler(36)
            clearUponHandler(37)
            clearUponHandler(38)
            clearUponHandler(39)
            clearUponHandler(40)
            sendToLabel(9)
    sprite('ny202_f01', 2)
    sprite('ny202_f02', 2)
    sprite('ny202_f03', 2)
    sprite('ny202_f04', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 33)
    sprite('ny202_f05', 1)
    sprite('ny202_f05', 1)
    sprite('ny202_f06', 1)
    RotationAngle(3000)
    sprite('ny202_f06', 20)
    RotationAngle(0)
    sprite('ny202_f06', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(2)
    sprite('ny202_f06', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 34)
    sprite('ny202_f07', 1)
    RotationAngle(3000)
    sprite('ny202_f07', 1)
    RotationAngle(0)
    sprite('ny202_f08', 1)
    RotationAngle(3000)
    sprite('ny202_f08', 20)
    RotationAngle(0)
    sprite('ny202_f08', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(3)
    sprite('ny202_f08', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 35)
    sprite('ny202_f09', 1)
    RotationAngle(3000)
    sprite('ny202_f09', 1)
    RotationAngle(0)
    sprite('ny202_f10', 1)
    RotationAngle(3000)
    sprite('ny202_f10', 20)
    RotationAngle(0)
    sprite('ny202_f10', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(4)
    sprite('ny202_f10', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 36)
    sprite('ny202_f11', 1)
    RotationAngle(3000)
    sprite('ny202_f11', 1)
    RotationAngle(0)
    sprite('ny202_f12', 1)
    RotationAngle(3000)
    sprite('ny202_f12', 20)
    RotationAngle(0)
    sprite('ny202_f12', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(5)
    sprite('ny202_f12', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 37)
    sprite('ny202_f13', 1)
    RotationAngle(3000)
    sprite('ny202_f13', 1)
    RotationAngle(0)
    sprite('ny202_f14', 1)
    RotationAngle(3000)
    sprite('ny202_f14', 20)
    RotationAngle(0)
    sprite('ny202_f14', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(6)
    sprite('ny202_f14', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 38)
    sprite('ny202_f15', 1)
    RotationAngle(3000)
    sprite('ny202_f15', 1)
    RotationAngle(0)
    sprite('ny202_f16', 1)
    RotationAngle(3000)
    sprite('ny202_f16', 20)
    RotationAngle(0)
    sprite('ny202_f16', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(7)
    sprite('ny202_f16', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 39)
    sprite('ny202_f17', 1)
    RotationAngle(3000)
    sprite('ny202_f17', 1)
    RotationAngle(0)
    sprite('ny202_f18', 1)
    RotationAngle(3000)
    sprite('ny202_f18', 20)
    RotationAngle(0)
    sprite('ny202_f18', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(8)
    sprite('ny202_f18', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 40)
    loopRest()
    label(9)
    sprite('null', 1)
    ExitState()


@State
def Funnel5C_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        RemoveOnCallStateEnd(3)
        AttackLevel_(3)
        Damage(160)
        SingleProration(1)
        AirPushbackY(15000)
        AirUntechableTime(23)
        Hitstun(20)
        Hitstop(3)
        UseSlashHitspark(1)
        HitsparkSize(600)
        VoodooDamageMultiplier(2)
        CHStateIfCHStart(3)
        AddX(-30000)
        AddY(30000)
        E0EAEffectObjectZ(3)
        SetZVal(-1)
        PaletteIndex(0)
        RandSpeedX(-4000, 4000)
        RandSpeedY(-4000, 4000)

        def upon_33():
            HitboxMovement(3000, 250000)

        def upon_34():
            HitboxMovement(3000, 300000)

        def upon_35():
            HitboxMovement(3000, 350000)

        def upon_36():
            HitboxMovement(3000, 400000)

        def upon_37():
            HitboxMovement(3000, 450000)

        def upon_38():
            HitboxMovement(3000, 500000)

        def upon_39():
            HitboxMovement(3000, 550000)

        def upon_40():
            HitboxMovement(3000, 600000)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
        AttackOff()
    sprite('null', 1)
    sprite('null', 1)
    YSpeed(-10000)
    sprite('ny202_f18ex01', 2)
    PrivateSE('nyse_29')
    sprite('ny202_f00atk', 2)
    sprite('ny202_f01atk', 1)
    sprite('ny202_f02atk', 1)
    SetAcceleration(100)
    sprite('ny202_f02atk', 1)
    physicsYImpulse(0)
    physicsXImpulse(100000)
    sprite('ny202_f02atk', 4)
    RefreshMultihit()
    loopRest()
    label(580)
    sprite('ny202_f02atk', 20)
    SetAcceleration(0)
    XImpulseAcceleration(-2)
    EndAttack()
    BlendMode_Normal()
    AlphaValue(120)
    ConstantAlphaModifier(-10)
    CreateParticle('nyef_cfanneldel', 0)


@State
def NY_SumDDMultiSword():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 100)

        def upon_17():
            sendToLabel(1)
        AddX(356000)
        AddY(250000)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_SumMultiSwordBigmc', -1)
    label(0)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 8)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 9)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 10)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 11)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 12)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 13)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 14)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 15)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 16)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 17)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 18)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 19)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 20)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 21)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 22)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 23)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 24)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 25)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 26)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 27)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 28)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 29)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 30)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 31)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 32)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 33)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 4)


@State
def NY_MultiSword():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(130)
        MinimumDamage(10)
        AttackP2(79)
        SingleProration(1)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(80000)
        AirPushbackY(1000)
        YImpulseBeforeWallbounce(5)
        AirUntechableTime(40)
        WallbounceReboundTime(5)
        Hitstop(2)
        HitsparkSize(400)
        UseSlashHitspark(1)
        StarterRating(2)
        VoodooDamageMultiplier(2)
        CHStateIfCHStart(3)
        if SLOT_IsUnlimited:
            Damage(140)
        PaletteIndex(2)
        AlphaValue(0)
        SetZVal(-50)
        ContinueState(120)

        def upon_OPPONENT_HIT_OR_BLOCK():
            sendToLabel(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(2)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CollideWithWall(1)
        PrivateSE('nyse_00')
    sprite('vrnyef_mltswd00', 1)
    CreateObject('NY_SumMultiSwordMc', -1)
    AddX(-80000)
    ConstantAlphaModifier(40)
    physicsXImpulse(29900)
    sprite('vrnyef_mltswd01', 1)
    sprite('vrnyef_mltswd02', 1)
    sprite('vrnyef_mltswd03', 1)
    sprite('vrnyef_mltswd04', 1)
    sprite('vrnyef_mltswd05', 1)
    XImpulseAcceleration(600)
    label(0)
    sprite('vrnyef_mltswdatk', 2)
    CreateParticle('nyef_sumDDmultikksn00', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnyef_mltswdatk', 6)
    EndAttack()
    ConstantAlphaModifier(-30)
    EndMomentum(1)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-100)


@State
def NY_SumDDMultiSwordOD():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 150)

        def upon_17():
            sendToLabel(1)
        AddX(356000)
        AddY(250000)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_SumMultiSwordBigmcOD', -1)
    label(0)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 8)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 9)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 10)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 11)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 12)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 13)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 14)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 15)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 16)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 17)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 18)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 19)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 20)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 21)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 22)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 23)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 24)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 25)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 26)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 27)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 28)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 29)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 30)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 31)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 32)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 33)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    sprite('null', 4)
    TriggerUponForState('NY_SumMultiSwordBigmcOD', 32)


@State
def NY_MultiSwordOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(130)
        MinimumDamage(10)
        AttackP2(79)
        SingleProration(1)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(80000)
        AirPushbackY(1000)
        YImpulseBeforeWallbounce(5)
        AirUntechableTime(40)
        WallbounceReboundTime(5)
        Hitstop(2)
        HitsparkSize(400)
        UseSlashHitspark(1)
        StarterRating(2)
        VoodooDamageMultiplier(2)
        CHStateIfCHStart(3)
        AttackType(4)
        if SLOT_IsUnlimited:
            Damage(140)
        PaletteIndex(2)
        AlphaValue(0)
        SetZVal(-50)
        ContinueState(120)

        def upon_OPPONENT_HIT_OR_BLOCK():
            sendToLabel(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(2)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CollideWithWall(1)
        PrivateSE('nyse_00')
    sprite('vrnyef_mltswd00', 1)
    CreateObject('NY_SumMultiSwordMc', -1)
    AddX(-80000)
    ConstantAlphaModifier(40)
    physicsXImpulse(29900)
    sprite('vrnyef_mltswd01', 1)
    sprite('vrnyef_mltswd02', 1)
    sprite('vrnyef_mltswd03', 1)
    sprite('vrnyef_mltswd04', 1)
    sprite('vrnyef_mltswd05', 1)
    XImpulseAcceleration(600)
    label(0)
    sprite('vrnyef_mltswdatk', 2)
    CreateParticle('nyef_sumDDmultikksn00', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnyef_mltswdatk', 6)
    EndAttack()
    ConstantAlphaModifier(-30)
    EndMomentum(1)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-100)


@State
def monoeye_line():

    def upon_IMMEDIATE():
        Visibility(1)
        CallObject('MonoeyeLine')
        E0EAEffectPolyline('vr_monoeye.hip', 2000)
    sprite('null', 32767)


@State
def EF_ny300():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        AddY(-30000)
    sprite('vrnyef300_parts1_00', 2)
    sprite('vrnyef300_parts1_01', 2)
    sprite('vrnyef300_parts1_02', 2)
    sprite('vrnyef300_parts1_03', 2)
    sprite('vrnyef300_parts1_04', 2)
    CreateObject('EF_ny300_parts2', 0)
    PrivateSE('nyse_31')
    sprite('vrnyef300_parts1_05', 2)
    sprite('vrnyef300_parts1_06', 2)
    sprite('vrnyef300_parts1_07', 1)
    sprite('vrnyef300_parts1_08', 1)
    sprite('vrnyef300_parts1_09', 1)
    sprite('vrnyef300_parts1_10', 1)
    sprite('vrnyef300_parts1_11', 1)
    sprite('vrnyef300_parts1_12', 35)
    sprite('vrnyef300_parts1_12', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()
    CreateObject('DIST_NY5D', 0)
    CreateParticle('nyef_cfanneldel', 0)


@State
def EF_ny300_parts2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(275000)
        XPositionRelativeFacing(120000)
    sprite('vrnyef300_parts2_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts2_00', 3)
    SetScaleSpeedY(0)
    CreateObject('EF_ny300_parts3', 0)
    sprite('vrnyef300_parts2_00', 36)
    sprite('vrnyef300_parts2_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def EF_ny300_parts3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(320000)
        XPositionRelativeFacing(95000)
    sprite('vrnyef300_parts3_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts3_00', 1)
    CreateObject('EF_ny300_parts4', 0)
    sprite('vrnyef300_parts3_00', 30)
    sprite('vrnyef300_parts3_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def EF_ny300_parts4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(248000)
        XPositionRelativeFacing(30000)
    sprite('vrnyef300_parts5_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts5_00', 1)
    CreateObject('EF_ny300_parts5', 0)
    sprite('vrnyef300_parts5_00', 26)
    sprite('vrnyef300_parts5_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def EF_ny300_parts5():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(300000)
        XPositionRelativeFacing(36000)
    sprite('vrnyef300_parts4_00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts4_00', 22)
    sprite('vrnyef300_parts4_00', 12)
    PrivateSE('nyse_30')
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def EntryFallSword():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        SetZVal(500)
        BlendMode_Normal()
        AbsoluteY(760000)
        AddX(-140000)
    sprite('vrnyef600_swd', 12)
    physicsYImpulse(-60000)
    sprite('vrnyef600_swd', 5)
    physicsYImpulse(-2000)
    CreateParticle('nyef_entrymc', 104)
    sprite('vrnyef600_swd', 5)
    physicsYImpulse(-1000)
    sprite('vrnyef600_swd', 10)
    physicsYImpulse(-500)
    sprite('vrnyef600_swd', 10)
    sprite('vrnyef600_swd', 12)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('022_magiccircle_a')
    sprite('vrnyef600_swd', 6)
    CreateParticle('nyef_entrylightB', 0)


@State
def EntryFallSword_RGVsNY():

    def upon_IMMEDIATE():
        SetZVal(500)
        BlendMode_Normal()
        AbsoluteY(760000)
        AddX(-140000)
    sprite('vrnyef600_swd', 12)
    physicsYImpulse(-60000)
    sprite('vrnyef600_swd', 5)
    physicsYImpulse(-2000)
    CreateParticle('nyef_entrymc', 104)
    sprite('vrnyef600_swd', 5)
    physicsYImpulse(-1000)
    sprite('vrnyef600_swd', 10)
    physicsYImpulse(-500)
    sprite('vrnyef600_swd', 10)
    EndMomentum(1)
    uponSendToLabel(32, 1)
    label(0)
    sprite('vrnyef600_swd', 1)
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    sprite('vrnyef600_swd', 12)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('022_magiccircle_a')
    sprite('vrnyef600_swd', 6)
    CreateParticle('nyef_entrylightB', 0)


@State
def RLAstSmoke():

    def upon_IMMEDIATE():
        LinkParticle('nyef_rlAHsmoke')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
    sprite('null', 65)
    AlphaValue(0)
    ConstantAlphaModifier(3)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def Changering():

    def upon_IMMEDIATE():
        Eff3DEffect('nyef_modechange00', '')
        LinkParticle('nyef_changering_jizoku')
        FaceSpawnLocation()
        PaletteIndex(1)
        ColorFromPaletteIndex(83)
        BlendMode_Normal()
        AlphaValue(0)
        Size(380)

        def upon_16():
            PrivateFunction3(3, 0, 200000, 50, 1)
        uponSendToLabel(32, 0)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    sprite('null', 32767)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    CreateParticle('nyef_ringend_02', -1)
    clearUponHandler(32)
    ConstantAlphaModifier(-12)
    sprite('null', 1)
    ExitState()


@State
def ModeChangeEf():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(255)
        CallPrivateEffect('nyef_changeeff_addtb')
        AddY(250000)
    sprite('null', 30)
    sprite('null', 30)
    ConstantAlphaModifier(-9)


@State
def __407slash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(150)
        Size(950)
        Eff3DEffect('nyef_407slash', '')
        AddY(120000)
    sprite('null', 28)


@State
def NY_BackShot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(1000)
        AirPushbackY(-30000)
        UseSlashHitspark(1)
        GroundedHitstunAnimation(2)
        HardKnockdown(10)
        Size(1500)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        physicsXImpulse(5000)
        physicsYImpulse(-4000)
        RotationSomething(0)
    sprite('vrnyef_swde00', 1)
    sprite('vrnyef_swde01', 1)
    sprite('vrnyef_swde02', 1)
    sprite('vrnyef_swde03', 1)
    sprite('vrnyef_swde04', 1)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrnyef_swde05', 1)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrnyef_swdeatk', 30)
    XImpulseAcceleration(200)
    YAccel(200)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def TimelagShot_Obj_Summon():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Unknown4024(3)
        AbsoluteY(600000)
        PaletteIndex(1)
        RunLoopUpon(17, 240)

        def upon_17():
            clearUponHandler(17)
            clearUponHandler(32)
            clearUponHandler(41)
            clearUponHandler(EVERY_FRAME)
            clearUponHandler(PLAYER_BLOCKS)
            sendToLabel(9)

        def upon_32():
            clearUponHandler(17)
            clearUponHandler(32)
            clearUponHandler(41)
            clearUponHandler(EVERY_FRAME)
            clearUponHandler(PLAYER_BLOCKS)
            sendToLabel(9)

        def upon_41():
            clearUponHandler(17)
            clearUponHandler(32)
            clearUponHandler(41)
            clearUponHandler(EVERY_FRAME)
            clearUponHandler(PLAYER_BLOCKS)
            sendToLabel(1)
        SLOT_9 = 1

        def upon_STATE_END():
            SLOT_9 = 0
        CopyFromRightToLeft(23, 2, 51, 3, 2, 58)
    sprite('null', 20)
    ParticleColorFromPalette(229, 225, 229)
    CallCustomizableParticle('nyef_411_add', -1)
    CreateParticle('nyef_sumA03', -1)
    CreateParticle('nyef_411', -1)
    PrivateSE('nyse_30')
    label(0)
    sprite('null', 20)
    CreateParticle('nyef_sumA03', -1)
    CreateParticle('nyef_411', -1)
    PrivateSE('nyse_34')
    loopRest()
    gotoLabel(0)
    label(1)

    def upon_PLAYER_BLOCKS():
        clearUponHandler(PLAYER_BLOCKS)
        sendToLabel(0)

        def upon_41():
            clearUponHandler(17)
            clearUponHandler(32)
            clearUponHandler(41)
            clearUponHandler(EVERY_FRAME)
            clearUponHandler(PLAYER_BLOCKS)
            sendToLabel(1)
    sprite('null', 20)
    CreateParticle('nyef_sumA03', -1)
    CreateParticle('nyef_411', -1)
    sprite('null', 10)
    CreateParticle('nyef_sumA03', -1)
    CreateParticle('nyef_411', -1)
    CreateObject('TimelagShot_Obj', -1)
    sprite('null', 10)
    if SLOT_51:
        CreateObject('TimelagShot_Obj', -1)
    loopRest()
    gotoLabel(100)
    label(9)
    sprite('null', 10)
    CreateParticle('nyef_sumA03', -1)
    CreateParticle('nyef_411', -1)
    CreateObject('TimelagShot_Obj', -1)
    sprite('null', 10)
    if SLOT_51:
        CreateObject('TimelagShot_Obj', -1)
    loopRest()
    gotoLabel(100)
    label(100)
    sprite('null', 40)


@State
def TimelagShot_Obj():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        AttackP1(80)
        SameMoveProration(10)
        GroundedHitstunAnimation(9)
        AirPushbackY(18000)
        AirUntechableTime(33)
        PushbackX(19800)
        UseSlashHitspark(1)
        StarterRating(1)
        VoodooDamageMultiplier(2)
        Size(1500)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AbsoluteY(600000)
        Unknown1111(8000, 22)
        ContinueState(100)
        CollideWithWall(1)
        if SLOT_9 == 1:
            Damage(1000)
            SetActionMark(1)
            Unknown1111(12000, 22)
        if SLOT_9 == 2:
            Damage(800)
        if SLOT_9 == 3:
            Damage(800)
        HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)

        def upon_LANDING():
            sendToLabel(580)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 1)
    SpriteIfNot0(11, 2, 2)
    XImpulseAcceleration(1)
    YAccel(1)
    sprite('vrnyef_411swd00', 1)
    if random_(2, 0, 33):
        PrivateSE('nyse_23')
    elif random_(2, 0, 50):
        PrivateSE('nyse_24')
    else:
        PrivateSE('nyse_25')
    XImpulseAcceleration(10000)
    YAccel(10000)
    sprite('vrnyef_411swd01', 1)
    sprite('vrnyef_411swd02', 1)
    sprite('vrnyef_411swd03', 1)
    sprite('vrnyef_411swd04', 1)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrnyef_411swd05', 1)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrnyef_411swdatk', 32767)
    XImpulseAcceleration(200)
    YAccel(200)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    EndAttack()
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')
    EndAttack()


@State
def BurstDD_Shot():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(600)
        AttackP1(125)
        AttackP2(80)
        MinimumDamage(0)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Stagger(200)
        Crumple(200)
        UseSlashHitspark(1)
        OnlyHitPlayer(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        DamageFromStateOnly('BurstDD_MultShot')
        Hitstop(20)
        Blockstun(26)
        CounterHitSetting(1)
        AutoHitStopSending(1)
        MinimumDamage(10)
        AddX(200000)
        AddY(200000)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_OPPONENT_HIT():
            TriggerUponForState('BurstDD', 40)
            TriggerUponForState('BurstDD_Easy', 40)
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(19800)
            ObjectUpon(EVERY_FRAME, 32)
    sprite('vrnyef_mltswd00', 1)
    CreateObject('NY_SumMultiSwordMc', -1)
    physicsXImpulse(22000)
    if random_(2, 0, 33):
        PrivateSE('nyse_23')
    elif random_(2, 0, 50):
        PrivateSE('nyse_24')
    else:
        PrivateSE('nyse_25')
    sprite('vrnyef_mltswd01', 1)
    sprite('vrnyef_mltswd02', 1)
    sprite('vrnyef_mltswd03', 1)
    sprite('vrnyef_mltswd04', 1)
    sprite('vrnyef_mltswd05', 1)
    sprite('vrnyef_mltswdatk', 2)
    CreateParticle('nyef_sumDDmultikksn00', -1)
    sprite('vrnyef_mltswdatk', 1)
    CreateParticle('nyef_sumDDmultikksn00', -1)
    sprite('vrnyef_mltswdatk', 1)
    XImpulseAcceleration(375)
    sprite('vrnyef_mltswdatk', 2)
    CreateParticle('nyef_sumDDmultikksn00', -1)
    sprite('vrnyef_mltswdatk', 2)
    CreateParticle('nyef_sumDDmultikksn00', -1)
    sprite('vrnyef_mltswdatk', 2)
    CreateParticle('nyef_sumDDmultikksn00', -1)
    sprite('vrnyef_mltswdatk', 2)
    NoAttackDuringAction(1)
    XImpulseAcceleration(50)
    AlphaValue(200)
    ConstantAlphaModifier(-20)
    sprite('vrnyef_mltswdatk', 2)
    XImpulseAcceleration(50)
    sprite('vrnyef_mltswdatk', 2)
    XImpulseAcceleration(50)
    sprite('vrnyef_mltswdatk', 2)
    XImpulseAcceleration(50)
    sprite('vrnyef_mltswdatk', 2)
    XImpulseAcceleration(0)


@State
def BurstDD_ShotMato():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
        TeleportToObject(22)
        AddY(500000)
        AddX(200000)
        SLOT_8 = 0
    sprite('null', 12)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(72)
    sprite('null', 12)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(63)
        SetZVal(500)
        AddX(180000)
        AddY(120000)
    sprite('null', 8)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(54)
        AddX(-180000)
        AddY(-120000)
    sprite('null', 8)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(49)
        AddX(-180000)
        AddY(120000)
    sprite('null', 8)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(44)
        SetZVal(500)
        AddX(180000)
        AddY(-120000)
    sprite('null', 60)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(39)
        SLOT_52 = 1
        AddY(-200000)
    ObjectUpon(EVERY_FRAME, 32)
    label(0)
    sprite('null', 2)


@State
def BurstDD_ShotMatoSP():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
        TeleportToObject(22)
        AddY(650000)
        AddX(300000)
        SLOT_8 = 0
    sprite('null', 6)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(63)
    sprite('null', 3)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(59)
        SetZVal(500)
        AddX(150000)
        AddY(100000)
    sprite('null', 3)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(55)
        AddX(-150000)
        AddY(-100000)
    sprite('null', 3)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(54)
        AddX(-150000)
        AddY(100000)
    sprite('null', 3)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(53)
        SetZVal(500)
        AddX(150000)
        AddY(-100000)
    sprite('null', 2)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(52)
        AddY(-200000)
    sprite('null', 2)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(52)
        AddX(-300000)
    sprite('null', 2)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(52)
        AddY(200000)
    sprite('null', 2)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(52)
        SetZVal(500)
        AddX(300000)
    sprite('null', 2)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(52)
        SetZVal(500)
        AddX(300000)
        AddY(-200000)
    sprite('null', 2)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(52)
        AddX(-300000)
        AddY(200000)
    sprite('null', 2)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(52)
        AddX(-300000)
        AddY(-200000)
    sprite('null', 2)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(52)
        SetZVal(500)
        AddX(300000)
        AddY(200000)
    sprite('null', 2)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(52)
        SetZVal(500)
        AddX(150000)
        AddY(-300000)
    sprite('null', 120)
    CreateObject('BurstDD_ShotEx', -1)

    def RunOnObject_1():
        SetActionMark(52)
        SLOT_52 = 1
        AddX(-150000)
        AddY(-300000)
    ObjectUpon(EVERY_FRAME, 32)
    label(0)
    sprite('null', 2)


@State
def BurstDD_ShotEx():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        EnableAfterimage(1)
        Flip()
        uponSendToLabel(LANDING, 2)

        def upon_EVERY_FRAME():
            AddActionMark(-1)
            if not SLOT_2:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(1)
    sprite('null', 1)
    PrivateSE('nyse_35')
    label(0)
    sprite('null', 6)
    CreateObject('BurstDD_MC', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 6)
    CreateObject('BurstDD_MC', 0)
    CreateObject('BurstDD_MultShot', 0)
    sprite('null', 6)
    CreateObject('BurstDD_MC', 0)
    sprite('null', 6)
    CreateObject('BurstDD_MC', 0)
    sprite('null', 6)
    CreateObject('BurstDD_MC', 0)
    label(2)
    sprite('null', 10)
    SLOT_8 = SLOT_52
    enterState('BurstDD_MultShot')


@State
def BurstDD_MultShot():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(197)
        MinimumDamage(0)
        AttackP2(100)
        SameMoveProration(-1)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Hitstop(4)
        PushbackX(-9800)
        Stagger(45)
        Crumple(9999)
        HardKnockdown(15)
        FlipOnHit(1)
        HitsparkSize(500)
        UseSlashHitspark(1)
        OnlyHitPlayer(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        DamageFromStateOnly('BurstDD_MultShot')
        DefeatOpponentBehavior(1)
        MinimumDamage(10)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 51)
        if SLOT_51:
            Damage(170)
            Stagger(15)
        if SLOT_8:
            AttackType(4)
            DefeatOpponentBehavior(0)
            SLOT_8 = 0
        AttackOff()
        EnableAfterimage(1)

        def upon_OPPONENT_HIT():
            ScreenShake(2000, 2000)
        uponSendToLabel(LANDING, 2)
    sprite('vrnyef_swdi00', 2)
    sprite('vrnyef_swdi01', 2)
    sprite('vrnyef_swdi02', 2)
    sprite('vrnyef_swdi03', 2)
    sprite('vrnyef_swdi04', 2)
    sprite('vrnyef_swdiatk', 2)
    physicsXImpulse(15000)
    physicsYImpulse(-30000)
    sprite('vrnyef_swdiatk', 2)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrnyef_swdiatk', 32767)
    XImpulseAcceleration(200)
    YAccel(200)
    RefreshMultihit()
    label(2)
    sprite('vrnyef_swdiatk', 1)
    HitAnywhere(1)
    EndMomentum(1)
    ScreenShake(5000, 5000)
    sprite('vrnyef_swdi10', 2)
    sprite('vrnyef_swdi11', 10)
    sprite('vrnyef_swdi11', 10)
    CreateParticle('nyef_sumB', -1)
    BlendMode_Normal()
    ConstantAlphaModifier(-26)


@State
def BurstDD_MC():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AddY(150000)
        AddX(-50000)
    sprite('null', 1)
    CallCustomizableParticle('nyef_440_sub', -1)
    ParticleLayer(11)
    ParticleColorFromPalette(225, 225, 226)
    CallCustomizableParticle('nyef_440_mc', -1)


@State
def BurstDD_DummyCamera():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraPosition(1200)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 51)
        if SLOT_51:
            CameraPosition(1500)
        TeleportToObject(22)
        uponSendToLabel(41, 9)
    sprite('null', 32767)
    label(9)
    sprite('null', 10)
    CameraControlEnable(0)
    CameraPosition(-1)


@State
def NY_Sword4D_Event():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')

        def upon_32():
            if SLOT_19 > 600000:
                TeleportToObject(22)
                AddX(100000)
            else:
                AddX(650000)
                AddX(100000)
            AbsoluteY(580000)
            CreateObject('NY_SummonA', 0)

        def upon_33():
            if SLOT_19 > 600000:
                TeleportToObject(22)
                AddX(-25000)
            else:
                AddX(625000)
            AbsoluteY(580000)
            CreateObject('NY_SummonA', 0)
        physicsXImpulse(-1666)
        physicsYImpulse(-4333)
        RotationSomething(0)
        PushbackX(-20000)
        HitOverhead(2)
    sprite('vrnyef_swdd00', 4)
    AttackOff()
    sprite('vrnyef_swdd01', 4)
    sprite('vrnyef_swdd02', 4)
    sprite('vrnyef_swdd03', 4)
    sprite('vrnyef_swdd04', 3)
    sprite('vrnyef_swdd05', 3)
    sprite('vrnyef_swddatk', 3)
    XImpulseAcceleration(1100)
    YAccel(1100)
    sprite('vrnyef_swddatk', 2)
    RefreshMultihit()
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def EventRL():

    def upon_IMMEDIATE():
        PaletteIndex(7)
        XPositionRelativeFacing(1060000)
    sprite('rl000_00', 8)
    Flip()
    label(0)
    sprite('rl000_01', 8)
    sprite('rl000_02', 8)
    sprite('rl000_03', 8)
    sprite('rl000_04', 8)
    sprite('rl000_05', 8)
    sprite('rl000_06', 8)
    sprite('rl000_07', 8)
    sprite('rl000_00', 8)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_Nirvana():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        EnableCollision(0)
        LoadSpritePalette(0)
        XPositionRelativeFacing(-260000)
        SetZVal(1000)
        uponSendToLabel(41, 9)
    sprite('ca805_09', 32767)
    loopRest()
    label(9)
    sprite('null', 2)


@State
def Act2Event_Carl():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        EnableCollision(0)
        LoadSpritePalette(0)
        XPositionRelativeFacing(-360000)
        SetZVal(500)
        uponSendToLabel(32, 0)
        uponSendToLabel(41, 9)
    sprite('ca070_03', 32767)
    loopRest()
    label(0)
    sprite('ca070_03', 20)
    sprite('ca070_10', 4)
    sprite('ca070_11', 4)
    sprite('ca070_12', 4)
    sprite('ca070_13', 4)
    label(1)
    sprite('ca000_00', 6)
    sprite('ca000_01', 6)
    sprite('ca000_02', 6)
    sprite('ca000_03', 6)
    sprite('ca000_04', 6)
    sprite('ca000_05', 6)
    sprite('ca000_06', 6)
    sprite('ca000_07', 6)
    sprite('ca000_08', 6)
    sprite('ca000_09', 6)
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('null', 2)


@State
def Act2Event_Bang():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        ScreenCollision(0)
        LoadSpritePalette(0)
        XPositionRelativeFacing(-360000)
        StayAfterMovement(1, 0)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(LANDING, 9)
    sprite('bn070_03', 32767)
    loopRest()
    label(0)
    sprite('bn070_03', 20)
    sprite('bn070_04', 4)
    sprite('bn070_05', 4)
    sprite('bn070_06', 4)
    sprite('bn070_07', 4)
    sprite('bn070_08', 4)
    sprite('bn070_09', 4)
    sprite('bn063_11', 4)
    AddX(130000)
    LandingEffects(0, 1, 1)
    CommonSE('209_down_normal_0')
    sprite('bn063_11', 32767)
    loopRest()
    label(1)
    sprite('bn064_00', 4)
    sprite('bn064_01', 4)
    sprite('bn064_02', 4)
    sprite('bn064_03', 4)
    sprite('bn064_04', 4)
    sprite('bn064_05', 4)
    sprite('bn064_06', 4)
    sprite('bn064_07', 4)
    sprite('bn064_08', 4)
    sprite('bn064_09', 4)
    sprite('bn064_10', 4)
    sprite('bn064_11', 4)
    loopRest()
    label(100)
    sprite('bn000_00', 7)
    sprite('bn000_01', 7)
    sprite('bn000_02', 7)
    sprite('bn000_03', 7)
    sprite('bn000_04', 7)
    sprite('bn000_05', 7)
    sprite('bn000_06', 7)
    sprite('bn000_07', 7)
    sprite('bn000_08', 7)
    sprite('bn000_09', 7)
    sprite('bn000_11', 7)
    loopRest()
    gotoLabel(100)
    label(2)
    sprite('keep', 2)
    sprite('bn023_00', 6)
    sprite('bn023_01', 6)
    sprite('bn022_00', 5)
    physicsXImpulse(-30000)
    physicsYImpulse(36000)
    setGravity(1800)
    JumpEffects(0, 0)
    CommonSE('001_airbackdash_0')
    sprite('bn022_01', 5)
    sprite('bn022_02', 5)
    sprite('bn022_03', 5)
    sprite('bn022_04', 5)
    sprite('bn022_05', 5)
    sprite('bn022_06', 5)
    label(101)
    sprite('bn022_07', 7)
    sprite('bn022_08', 7)
    loopRest()
    gotoLabel(101)
    label(9)
    sprite('null', 2)
    loopRest()


@State
def Event_EF_ny300():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        AddY(-30000)

        def upon_32():
            TriggerUponForState('Event_EF_ny300_parts2', 32)
            TriggerUponForState('Event_EF_ny300_parts3', 32)
            TriggerUponForState('Event_EF_ny300_parts4', 32)
            TriggerUponForState('Event_EF_ny300_parts5', 32)
            sendToLabel(0)
    sprite('vrnyef300_parts1_00', 2)
    sprite('vrnyef300_parts1_01', 2)
    sprite('vrnyef300_parts1_02', 2)
    sprite('vrnyef300_parts1_03', 2)
    sprite('vrnyef300_parts1_04', 2)
    CreateObject('Event_EF_ny300_parts2', 0)
    PrivateSE('nyse_31')
    sprite('vrnyef300_parts1_05', 2)
    sprite('vrnyef300_parts1_06', 2)
    sprite('vrnyef300_parts1_07', 1)
    sprite('vrnyef300_parts1_08', 1)
    sprite('vrnyef300_parts1_09', 1)
    sprite('vrnyef300_parts1_10', 1)
    sprite('vrnyef300_parts1_11', 1)
    sprite('vrnyef300_parts1_12', 32767)
    loopRest()
    label(0)
    sprite('vrnyef300_parts1_12', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()
    CreateObject('DIST_NY5D', 0)
    CreateParticle('nyef_cfanneldel', 0)


@State
def Event_EF_ny300_parts2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(275000)
        XPositionRelativeFacing(120000)

        def upon_32():
            sendToLabel(0)
    sprite('vrnyef300_parts2_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts2_00', 3)
    SetScaleSpeedY(0)
    CreateObject('Event_EF_ny300_parts3', 0)
    sprite('vrnyef300_parts2_00', 32767)
    loopRest()
    label(0)
    sprite('vrnyef300_parts2_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def Event_EF_ny300_parts3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(320000)
        XPositionRelativeFacing(95000)

        def upon_32():
            sendToLabel(0)
    sprite('vrnyef300_parts3_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts3_00', 1)
    CreateObject('Event_EF_ny300_parts4', 0)
    sprite('vrnyef300_parts3_00', 32767)
    loopRest()
    label(0)
    sprite('vrnyef300_parts3_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def Event_EF_ny300_parts4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(248000)
        XPositionRelativeFacing(30000)

        def upon_32():
            sendToLabel(0)
    sprite('vrnyef300_parts5_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts5_00', 1)
    CreateObject('Event_EF_ny300_parts5', 0)
    sprite('vrnyef300_parts5_00', 32767)
    loopRest()
    label(0)
    sprite('vrnyef300_parts5_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def Event_EF_ny300_parts5():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(300000)
        XPositionRelativeFacing(36000)

        def upon_32():
            sendToLabel(0)
    sprite('vrnyef300_parts4_00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts4_00', 32767)
    loopRest()
    label(0)
    sprite('vrnyef300_parts4_00', 12)
    PrivateSE('nyse_30')
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def Event_SummonDDBigSword():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AddX(406000)
        AddY(640000)
        SetZVal(-1)
        AlphaValue(0)
        WallCollisionDetection(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageColor_1(0, 255, 0, 0)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1030)
        AfterimageSize_2(1040)
        NoAttackDuringAction(1)
    sprite('vrnyef_ddbigswd00', 11)
    CreateObject('NY_SumBigSword', -1)
    CreateObject('Event_SummonDDBigSwordSub', -1)
    ConstantAlphaModifier(10)
    AddY(512000)
    physicsYImpulse(-1000)
    CreateParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd01', 1)
    AddY(-200000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    ScreenShake(0, 30000)
    PrivateSE('nyse_04')
    sprite('vrnyef_ddbigswd02', 1)
    AddY(-150000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd03', 1)
    AddY(-50000)
    CreateParticle('nyef_sumDDshock', 104)
    CreateParticle('nyef_sumDDshocklight00', 0)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd04', 20)
    AlphaValue(255)
    SetScaleSpeed(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    sprite('vrnyef_ddbigswd05', 25)
    physicsYImpulse(2000)
    ConstantAlphaModifier(-10)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)


@State
def Event_SummonDDBigSwordSub():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(1)
        SetZVal(-5)
        ContinueState(120)
        AlphaValue(0)
        WallCollisionDetection(1)
        EnableAfterimage(0)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(5)
        AfterimageColor_1(0, 255, 0, 0)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1020)
        AfterimageSize_2(1050)
    sprite('vrnyef_ddbigswdb00', 11)
    AddY(512000)
    physicsYImpulse(-500)
    ConstantAlphaModifier(20)
    sprite('vrnyef_ddbigswdb01', 1)
    AddY(-200000)
    sprite('vrnyef_ddbigswdb02', 1)
    AddY(-150000)
    sprite('vrnyef_ddbigswdb03', 1)
    AddY(-50000)
    sprite('vrnyef_ddbigswdb04', 20)
    physicsYImpulse(-500)
    AlphaValue(255)
    sprite('vrnyef_ddbigswdb05', 10)
    sprite('vrnyef_ddbigswdb05', 15)
    ConstantAlphaModifier(-20)


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def Act2Event_Camera_nyvspt():
    sprite('null', 32767)
    ScreenCollision(0)
    XPositionRelativeFacing(2500000)
    CameraControlEnable(1)


@State
def Act2EventSummonSlowArea():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)

        def upon_32():
            AddX(400000)

        def upon_35():
            CreateParticle('nyef_slowfieldend', -1)
            DeleteObject(23)

        def upon_33():
            sendToLabel(1)

        def upon_STATE_END():
            pass
    sprite('null', 1)
    sprite('null', 20)
    CreateObject('NY_SlowFieldStart', -1)
    PrivateSE('nyse_02')
    SlowField(1)
    label(0)
    sprite('null', 20)
    CreateObject('NY_SlowField', -1)
    CommonSE('022_magiccircle_c')
    sprite('null', 20)
    CreateObject('NY_SlowField', -1)
    sprite('null', 20)
    CreateObject('NY_SlowField', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 20)
    TriggerUponForState('Act2Event_moyamoya', 32)
    CreateParticle('nyef_slowfieldend', -1)


@State
def Act2Event_moyamoya():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AddX(370000)
        AddY(-157500)
        Size(2000000000)
        SetZVal(-100)
        uponSendToLabel(32, 1)
    sprite('null', 2)
    label(0)
    sprite('null', 5)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('null', 2)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    loopRest()


@State
def Act2EventEffBarrier():

    def upon_IMMEDIATE():
        Eff3DEffect('ef_gird_f.DIG', 'ef_gird_f_motion_000.mmot')
        FaceSpawnLocation()
        CreateObject('Act2EventEffBarrierParts', -1)
        AbsoluteY(0)
        XPositionRelativeFacing(0)
        E0EAEffectPositionCenter(3)
        E0EAEffectDirection(3)
        Visibility(1)
        BlendMode_Add()
        AlphaValue(0)
    label(0)
    sprite('null', 5)
    SetScaleSpeed(0)
    ConstantAlphaModifier(0)
    ConstantAlphaModifier(12)
    Size(1500)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(-85)
    SetScaleSpeed(30)


@State
def Act2EventEffBarrierParts():

    def upon_IMMEDIATE():
        LinkParticle('ef_gird_f')
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        Size(1500)
    sprite('null', 32767)


@State
def Act2EventSumDDMultiSword():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 30)

        def upon_17():
            AddScale(100001)
        AddX(106000)
        AddY(250000)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_SumMultiSwordBigmc', -1)
    label(1)
    sprite('null', 4)

    def RunOnObject_1():
        AddScale(10000)


@State
def Act2AZvsNY_SumDDMultiSword():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 180)

        def upon_17():
            sendToLabel(1)
        AddX(286000)
        AddY(250000)

        def upon_STATE_END():
            ObjectUpon(22, 32)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_SumMultiSwordBigmc', -1)
    label(0)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 8)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 9)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 10)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 11)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 12)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 13)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 14)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 15)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 16)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 17)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 18)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 19)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 20)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 21)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 22)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 23)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 24)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 25)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 26)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 27)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 28)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 29)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 30)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 31)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 32)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 33)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 36)
    loopRest()


@State
def Act3Event_TeniObj():

    def upon_IMMEDIATE():
        pass
    sprite('null', 80)
    CreateParticle('story_teni', 100)
    CommonSE('000_airdash_2')
    CommonSE('022_magiccircle_b')
    sprite('null', 3)
    CreateParticle('haef_event_lose_end', 103)
    loopRest()


@State
def Act3Event_NY_SumDDMultiSword():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 60)

        def upon_17():
            sendToLabel(1)
        AddY(250000)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_SumMultiSwordBigmc', -1)
    label(0)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 8)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 9)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 10)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 11)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 12)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 13)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 14)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 15)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 16)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 17)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 18)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 19)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 20)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 21)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 22)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 23)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 24)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 25)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 26)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 27)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 28)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 29)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 30)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 31)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 32)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('Act3Event_NY_MultiSword', 33)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 4)


@State
def Act3Event_NY_MultiSword():

    def upon_IMMEDIATE():
        NoAttackDuringAction(1)
        PaletteIndex(2)
        AlphaValue(0)
        SetZVal(-50)
        ContinueState(120)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(2)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CollideWithWall(1)
        PrivateSE('nyse_00')

        def upon_EVERY_FRAME():
            if SLOT_29 <= 180000:
                CreateObject('Act3Event_Guard', -1)
                clearUponHandler(EVERY_FRAME)
                EndMomentum(1)
                sendToLabel(1)
    sprite('vrnyef_mltswd00', 1)
    CreateObject('NY_SumMultiSwordMc', -1)
    AddX(-80000)
    ConstantAlphaModifier(40)
    physicsXImpulse(29900)
    sprite('vrnyef_mltswd01', 1)
    sprite('vrnyef_mltswd02', 1)
    sprite('vrnyef_mltswd03', 1)
    sprite('vrnyef_mltswd04', 1)
    sprite('vrnyef_mltswd05', 1)
    XImpulseAcceleration(600)
    label(0)
    sprite('vrnyef_mltswdatk', 2)
    CreateParticle('nyef_sumDDmultikksn00', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnyef_mltswdatk', 6)
    EndAttack()
    ConstantAlphaModifier(-30)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-100)


@State
def Act3Event_Guard():
    sprite('null', 4)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdm', 103)
    CommonSE('105_guard_slash_2')


@State
def Act3Event_teni():
    sprite('null', 1)
    sprite('null', 4)
    CreateParticle('haef_event_lose', 103)
    CommonSE('000_airdash_2')
